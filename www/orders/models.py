from collections.abc import Iterable
from django.db import models
from django.conf import settings
from shop.models import ProductVarietie,ProductGrade
from .utils import generateID36
import datetime
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError



class Order(models.Model):
    """
    """
    reference_id = models.SlugField(unique=True,default=generateID36)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    datestamp = models.DateField(auto_now_add=True)
    delivery_address= models.TextField(blank=True,null=True)
    delivery_parish = models.CharField(default="None",max_length=256)
    delivery_instructions = models.TextField(null=True,blank=True)
    delivery_phone = models.CharField(max_length=256,default="None")
    delivery_option = models.CharField(max_length=256,default="None")
    delivery_time = models.CharField(max_length=256,default="Pending")
    order_status= models.CharField(max_length=128,default='Draft')
    fulfilment_status = models.CharField(max_length=512,default='Unfulfilled')
    payment_status = models.CharField(max_length=512,default='Pending')
    hasCredit = models.BooleanField(default=False)
    creditUsed = models.CharField(max_length=256,null=True,blank=True)
    Amountpaid = models.CharField(max_length=128,default="0")
    payment_method = models.CharField(max_length=256,null=True,blank=True)

    @property
    def get_refidb64_token(self) -> str:
        token = urlsafe_base64_encode(force_bytes(self.reference_id))
        return token
    @property
    def transaction_id(self):
        number_string = str(self.pk).zfill(5)
        id = f"GR8W{number_string}"
        return id
    @property
    def grandtotal(self) -> float:
        total = sum([item.subtotal for item in self.orderitem_set.all()])
        return total
    @property
    def discount(self) -> float:
        total = sum([item.discount_total for item in self.orderitem_set.all()])
        return total
    @property
    def est_taxes(self) ->float:
        fee = 0.0
        return fee

    @property
    def servicefee(self) ->float:
        fee = 0.0
        return fee

    @property
    def deliveryfee(self) -> float:
        fee = 0.0
        return fee

    @property
    def total(self) -> float:
        grandtotal = (self.grandtotal + self.deliveryfee + self.servicefee + self.est_taxes) - self.discount
        return grandtotal
    
    @property
    def amountdue(self) -> float:
        total = self.total - float(self.Amountpaid)
        return total
    @property
    def date_in_mm_dd_yyyy(self):
        date = self.timestamp.strftime("%m-%d-%Y")
        return date
    @property
    def get_fulfilment_count(self):
        items = self.orderitem_set.filter(fulfilment_status=True)
        return items.count()
    
    @property
    def get_unfulfilment_count(self):
        items = self.orderitem_set.filter(fulfilment_status=False)
        return items.count()
    
    @property
    def get_fulfilment_set(self):
        items = self.orderitem_set.filter(fulfilment_status=True)
        return items
    
    @property
    def get_unfulfilment_set(self):
        items = self.orderitem_set.filter(fulfilment_status=False)
        return items
    
    @property
    def arrival_date(self)->str:
        pass

    def __str__(self) -> str:
        return f"{self.transaction_id} | {self.total}"
    
    def save(self, *args, **kwargs) -> None:
        if self.delivery_address == None:
            address = self.user.useraddress_set.get(default_status=True)
            self.delivery_address = f"{address.address_line1},\n{address.address_line2},\n{address.parish}"
            #self.save(update_fields=['delivery_address'])
        return super(Order, self).save(*args,**kwargs)
    

class OrderItem(models.Model):
    """
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVarietie,on_delete=models.DO_NOTHING,null=True,blank=True)
    product_grade = models.ForeignKey(ProductGrade,on_delete=models.DO_NOTHING)
    quantity = models.CharField(max_length=512,default='1')
    fulfilment_status = models.BooleanField(default=False)
    if_out_of_stock = models.TextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    price = models.CharField(max_length=512,null=True,blank=True)
    discount = models.CharField(max_length=256,blank=True,null=True)
    @property
    def subtotal(self):
        try:
            total = float(self.price.value) * float(self.quantity)
        except:
            total = float(self.product_grade.price.value) * float(self.quantity)
        return total
    @property
    def discount_total(self) -> float:
                try:
                    if self.discount.find('%') != -1:
                        discount_in_float = self.discount.split('%')
                        discount = (float(self.subtotal)  * ((float(discount_in_float[0])/100)))
                        return discount
                    elif float(self.discount) < 1.0:
                        discount = (float(self.subtotal)  * (float(self.discount)))
                        return discount
                    else:
                        discount = (float(self.discount) * float(self.quantity))
                        return discount
                except:
                    discount_in_float = 0.0
                    return discount_in_float
    
    def save(self, *args, **kwargs):

        if( self.price == None):
            self.price = self.product_grade.price.value
            #self.save(update_fields=['price'])

        return super(OrderItem,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return f"{self.order.transaction_id}  {self.product_grade.product.name} {self.product_grade.product.product.name} @ {self.product_grade.price} * {self.quantity} | {self.subtotal} {self.product_grade.price.currency} "

class OrderReplacement(models.Model):
    order_item = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    ProductGrade = models.ForeignKey(ProductGrade,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=512)
    fulfilment_status = models.BooleanField(default=False)
    price = models.CharField(max_length=512,null=True,blank=True)

    def save(self, *args, **kwargs):
        if( self.price == None):
            self.price = self.product_grade.price.value
            #self.save(update_fields=['price'])
        return super(OrderItem,self).save(*args,**kwargs)

class RecurringOrder(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True,blank=True)
    last_delivered = models.DateTimeField(auto_now=True)
    frequency = models.CharField(max_length=512)
    status = models.CharField(max_length=512)
    