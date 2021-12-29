from django.db import models
from store.models import Gig, Category
from users.models import Profile
import datetime

# Create your models here.

class Order(models.Model):
    product = models.ForeignKey(Gig,
                                on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
  
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_profile(profile_id):
        return Order.objects.filter(profile=profile_id).order_by('-date')

