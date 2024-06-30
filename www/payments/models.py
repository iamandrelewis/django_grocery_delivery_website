from django.db import models
from django.conf import settings
from orders import models as order_models

""
""

class PaymentMethod(models.Model):
    """
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    stripe_payment_method_id = models.CharField(max_length=512)

class OrderPayment(models.Model):
    """
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(order_models.Order,on_delete=models.CASCADE)
    amount = models.CharField(max_length=1024)
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.DO_NOTHING)

class MembershipPayment(models.Model):
    """
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    membership = models.CharField(max_length=1024)
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.DO_NOTHING)



