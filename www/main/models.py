from django.db import models
from users import models as m
from django.conf import settings

class UserAddress(models.Model):
    user = models.ForeignKey(m.CustomUser,on_delete=models.CASCADE,null=True)
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
    user = models.ForeignKey(m.CustomUser,on_delete=models.CASCADE,null=True)
    business_name = models.CharField(max_length=1024)
    business_category = models.CharField(max_length=1024)
    business_address = models.ForeignKey(UserAddress,on_delete=models.DO_NOTHING)

class UserMembership(models.Model):
    user = models.OneToOneField(m.CustomUser,on_delete=models.CASCADE,null=True)
    membership = models.CharField(max_length=256,default='Business')
    #status default="valid"
    # last_payment= DateTime auto_now=True

class UserRecovery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    two_step = models.BooleanField(default=False)
    recovery_email = models.EmailField()
    recovery_phone = models.CharField(max_length=256)


class UserSettings(models.Model):
    #send diagnostics
    #notification_order_update
    #notfification_promotions_update
    #notfication_delivery_update
    #notification_product_update
    #notification_prefered_method
    pass

class UserReferrals(models.Model):
    referee = models.ForeignKey(m.CustomUser,on_delete=models.CASCADE,related_name='referee',null=True)
    referer = models.ForeignKey(m.CustomUser,on_delete=models.CASCADE,related_name='referer',null=True)

class UserStoreCredit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=256)
    @property
    def creditLimit(self):
        try:
            credit = (sum([item.grandtotal for item in m.CustomUser.order_set.filter(payment_status="Paid")])) * 0.05
            credit += (sum([item.grandtotal for item in m.CustomUser.userreferrals_set.filter(referer=self.user).order_set.filter(payment_status="Paid")])) * 0.05
            print(m.CustomUser.userreferrals_set.filter(referer=self.user).order_set.filter(payment_status="Paid"))
            print(m.CustomUser.order_set.filter(payment_status="Paid"))
        except:
            credit = 0
        return credit
    
    @property
    def creditedTotal(self):
        try:
            credit = sum([item.creditUsed for item in m.CustomUser.order_set.filter(hasCredit=True)])
        except:
            credit = 0
        return credit
    
    @property
    def creditBalance(self):
        try:
            credit = self.creditLimit() - self.creditedTotal()
        except:
            credit = 0
        return credit