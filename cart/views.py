from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.base import View
from cart.models import Order

from store.models import Gig

# Create your views here.


class CheckOut(View):
    def post(self, request):
        gig_id = request.POST.get('gig_id', None)
        gig = Gig.get_gig_by_id(gig_id)

        order = Order(
                        profile=request.user.profile,
                        gig=gig,
                        price=gig.price,
                    )
        order.save()
        messages.success(request, "You successfully submited an order")
        return redirect('cart')


  
class OrderView(View):
    def get(self, request):
        orders = Order.get_orders_by_profile(request.user.profile.id)
        return render(request, 'orders.html', {'orders': orders})