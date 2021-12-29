from .models import Category

def provide_categories(request):
    nav_cats = Category.objects.all().order_by('-id')[:4]
    cats = Category.objects.all()
    return {'nav_cats': nav_cats, 'cats': cats}