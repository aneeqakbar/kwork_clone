from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import View, CreateView
from django.views.generic.detail import DetailView

from store.forms import CreateGigForm, CreatePackageForm
from store.models import Category, Gig

# Create your views here.

class HomeView(View):
    def get(self, request):
        gigs = Gig.objects.all().order_by('-id')
        context = {'gigs': gigs}
        return render(request, 'store/home.html', context)

# class ManageGigView(CreateView):
#     model = Gig
#     fields = ['name', 'price', 'image', 'description']
#     template_name = 'store/create-gig.html'

#     def form_valid(self, form):
#         category_name = self.request.POST.get('category', None)
#         category, created = Category.objects.get_or_create(name = category_name)
#         form.instance.profile = self.request.user.profile
#         form.instance.category = category
#         return super().form_valid(form)

class ManageGigView(View):
    def get(self, request):
        form = CreateGigForm()
        package_form = CreatePackageForm()
        context = {'form': form, 'package_form': package_form}
        return render(request, 'store/create-gig.html', context)

    def post(self, request):
        print(request.POST)
        form = CreateGigForm(request.POST, request.FILES)
        package_form = CreatePackageForm(request.POST)
        if form.is_valid() and package_form.is_valid():
            gig_ins = form.save(commit=False)
            category_name = self.request.POST.get('category', None)
            category = Category.objects.filter(name__iexact = category_name).first()

            if not category:
                category = Category.objects.create(name = category_name)

            gig_ins.profile = self.request.user.profile
            gig_ins.category = category
            gig_ins.save()

            prices = request.POST.getlist('price', None)
            package_descriptions = request.POST.getlist('package_description', None)
            deliverys = request.POST.getlist('delivery', None)
            package_types = request.POST.getlist('package_type', None)

            for i in range(3):
                try:
                    price = list(prices)[i]
                except:
                    price = None
                try:
                    package_description = list(package_descriptions)[i]
                except:
                    package_description = None
                try:
                    delivery = list(deliverys)[i]
                except:
                    delivery = None
                try:
                    source_file = request.POST.get(f'source_{i+1}', None)
                except:
                    source_file = None

                package_form = CreatePackageForm({
                'price': price,
                'package_description': package_description,
                'delivery': delivery,
                'source_file': source_file,
                })

                if package_form.is_valid():
                    package = package_form.save(commit = False)
                    package.gig = gig_ins
                    package.package_type = package_types[i]
                    package.save()

            return HttpResponseRedirect(gig_ins.get_absolute_url())

        context = {'form': form, 'package_form': package_form}
        return render(request, 'store/create-gig.html', context)


class GigDetailView(DetailView):
    model = Gig
    template_name = 'store/detail-gig.html'


class GigOrderView(View):
    def get(self, request, pk):
        package = request.GET.get('package', None)
        gig = get_object_or_404(Gig, pk = pk)
        package = gig.packages.filter(package_type = package).first()
        price = 0
        if package:
            price = package.price
        context = {'gig': gig, 'price': price}
        return render(request, 'store/order-page.html', context)