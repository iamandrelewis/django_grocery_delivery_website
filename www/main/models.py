from django.db import models
from users import models as m
from django.conf import settings
from .utils import generate_team_code
from orders.models import Order
import stripe


class UserAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    address_line1 = models.CharField(max_length= 512)
    address_line2 = models.CharField(max_length=256)
    parish = models.CharField(max_length=256)
    default_status = models.BooleanField(null=True,default=False)

    def save(self, *args, **kwargs):
        if self.default_status == True:
            for address in UserAddress.objects.filter(default_status=True):
                if self.user == address.user:
                    if address.default_status == self.default_status:
                        address.default_status = False
                        address.save(update_fields=['default_status'])
        return super(UserAddress, self).save(*args, **kwargs)

class UserBusiness(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    business_name = models.CharField(max_length=1024)
    business_category = models.CharField(max_length=1024)
    business_address = models.ForeignKey(UserAddress,on_delete=models.DO_NOTHING)

class UserMembership(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    membership = models.CharField(max_length=256,default='None',blank=True,null=True)
    status = models.CharField(max_length=256,default="Valid")
    #last_payment= DateTime auto_now=True
    @property
    def create_stripe_subscription_session(self,payment_method,membership_product,**kwargs):
        pass
    """@property
    def getNextPayment(self):
        try:
            next_payment = self.last_payment + relative+delta(months=+1)
        except:
            next_payment = None
        return next_payment
            """
    
class UserTeam(models.Model):
    code = models.CharField(max_length=10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    business = models.ForeignKey(UserBusiness,on_delete=models.CASCADE,null=True)


class UserRecovery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    two_step = models.BooleanField(default=False)
    recovery_email = models.EmailField()
    recovery_phone = models.CharField(max_length=256)


class UserSettings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    send_diagnostics = models.BooleanField(default=False)
    notification_order_update = models.BooleanField(default=False)
    notfification_promotions_update = models.BooleanField(default=False)
    notfication_delivery_update = models.BooleanField(default=False)
    notification_product_update = models.BooleanField(default=False)
    notification_prefered_method = models.CharField(max_length=512,default='Email')


class UserReferrals(models.Model):
    referee = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='referee',null=True)
    referer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='referer',null=True)

class UserStoreCredit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=256)

    @property
    def creditLimit(self):
        try:
            credit = (sum([item.grandtotal for item in self.user.order_set.filter(payment_status="Paid")])) * 0.05
            referrals = UserReferrals.objects.filter(referer=self.user)
            referees = list([str(i['referee_id']) for i in referrals.values()])
            for referee in referees:
                credit += (sum([order.grandtotal for order in Order.objects.filter(user_id=referee,payment_status="Paid")])) * 0.05
        except:
            credit = 0
        return credit
    
    @property
    def creditedTotal(self):
        try:
            credit = sum([item.creditUsed for item in self.user.order_set.filter(hasCredit=True)])
        except:
            credit = 0
        return credit
    
    @property
    def creditBalance(self):
        try:
            credit = self.creditLimit - self.creditedTotal
        except:
            credit = 0
        return credit
    
    def __str__(self) -> str:

        print(self.user.order_set.filter(payment_status="Paid"))
        return f' {  self.user} - { self.user.order_set.filter(hasCredit=True).count()} credited orders |  $J {self.creditLimit} remaining'