from django.db import models
from django.conf import settings
from orders.models import Order
# Create your models here.

class DeliverySession(models.Model):
    deliver_er = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=256)
    arrival_timestamp = models.DateTimeField(auto_now=True)

class PackSession(models.Model):
    pack_er = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=256)
    arrival_timestamp = models.DateTimeField(auto_now=True)