from typing import Iterable, Optional
from django.db import models
from django.conf import settings
from shop.models import ProductVarietie,ProductGrade
from .utils import generateID36

class Order(models.Model):
    reference_id = models.SlugField(unique=True,default=generateID36)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    @property
    def transaction_id(self):
        number_string = str(self.pk).zfill(5)
        id = f"GR8W{number_string}"
        return id
    timestamp = models.DateTimeField(auto_now_add=True)
    datestamp = models.DateField(auto_now_add=True)
    delivery_address= models.TextField(blank=True,null=True)
    delivery_instructions = models.TextField(null=True,blank=True)
    order_status= models.CharField(max_length=128,default='Draft')
    fulfilment_status = models.CharField(max_length=512,default='Unfufilled')
    payment_status = models.CharField(max_length=512,default='Pending')

    @property
    def grandtotal(self) -> float:
        total = sum([item.subtotal for item in self.orderitem_set.all()])
        return total
    
    def __str__(self) -> str:
        return f"{self.transaction_id} | {self.grandtotal}"
    
"""    def save(self, *args, **kwargs) -> None:
        if self.delivery_address == None:
            address = self.user.useraddress_set.get(default_status=True)
            self.delivery_address = f"{address.address_line1},\n{address.address_line2},\n{address.parish}"
            self.save(update_fields=['delivery_address'])
        return super(Order, self).save(*args,**kwargs)"""
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVarietie,on_delete=models.DO_NOTHING,null=True,blank=True)
    product_grade = models.ForeignKey(ProductGrade,on_delete=models.DO_NOTHING)
    quantity = models.CharField(max_length=512,default='1')
    fulfilment_status = models.BooleanField(default=False)
    if_out_of_stock = models.TextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    
    @property
    def subtotal(self):
        total = float(self.product_grade.price.value)*float(self.quantity)
        return total
    
    def __str__(self) -> str:
        return f"{self.order.transaction_id} {self.product} @ {self.product_grade.price} * {self.quantity} | {self.subtotal} {self.product_grade.price.currency} "

class OrderReplacement(models.Model):
    order_item = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    ProductGrade = models.ForeignKey(ProductGrade,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=512)
    fulfilment_status = models.BooleanField(default=False)