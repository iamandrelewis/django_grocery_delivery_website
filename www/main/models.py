from django.db import models
from users import models as m


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

class UserSettings(models.Model):
    pass

class UserReferrals(models.Model):
    referee = models.ForeignKey(m.CustomUser,on_delete=models.CASCADE,related_name='referee',null=True)
    referer = models.ForeignKey(m.CustomUser,on_delete=models.CASCADE,related_name='referer',null=True)

