from django.db import models
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
  
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
  
    def __str__(self):
        return self.name


class Gig(models.Model):
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE, related_name="gigs")
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/gig/')

    @staticmethod
    def get_gig_by_id(ids):
        return Gig.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_gig():
        return Gig.objects.all()
  
    @staticmethod
    def get_all_gig_by_categoryid(category_id):
        if category_id:
            return Gig.objects.filter(category=category_id)
        else:
            return Gig.get_all_gig()

    @property
    def get_basic_package(self):
        try:
            return self.packages.filter(package_type=1).order_by('-id').first()
        except:
            return None

    @property
    def get_standard_package(self):
        try:
            return self.packages.filter(package_type=2).order_by('-id').first()
        except:
            return None

    @property
    def get_premium_package(self):
        try:
            return self.packages.filter(package_type=3).order_by('-id').first()
        except:
            return None

    @property
    def get_all_packages(self):
        return list([self.get_basic_package,self.get_standard_package,self.get_premium_package])

    def get_absolute_url(self):
        return reverse('store:GigDetailView', kwargs={'pk': self.id})

PACKAGE_TYPES = (
    (1, 'Basic'),
    (2, 'Standard'),
    (3, 'Premium'),
)

class GigPackage(models.Model):
    gig = models.ForeignKey("store.Gig", on_delete=models.CASCADE, related_name="packages")
    price = models.IntegerField(default=0)
    package_description = models.TextField(null=True, blank=True)
    source_files = models.BooleanField(default=False)
    package_type = models.IntegerField(choices=PACKAGE_TYPES, null=True, blank=True)
    delivery = models.PositiveIntegerField(default=1)


# sk_test_ac9c389e97105d6033220fcdecddc451dd259bfc

# pk_test_260c5a2f79ad98f781f41ad29c177b5b15e07fc4