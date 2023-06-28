from django.db import models

class GreenProduceProductCategorie(models.Model):
    name = models.CharField(max_length=256)
    
class GreenProducePrice(models.Model):
    category = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
    currency = models.CharField(max_length=256)

class GreenProduceProduct(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(GreenProduceProductCategorie,on_delete=models.CASCADE,related_name='green_produce_category')

class GreenProduceProductImage(models.Model):
    green_produce_product = models.ForeignKey(GreenProduceProduct,on_delete=models.CASCADE,related_name='green_produce_image')
    image = models.ImageField(upload_to='products/')

class GreenProduceVarietie(models.Model):
    green_produce_product = models.ForeignKey(GreenProduceProduct,on_delete=models.CASCADE,related_name='green_produce_variety')
    name = models.CharField(max_length=256)
    
class GreenProduceUnit(models.Model):
    green_produce_product= models.ForeignKey(GreenProduceProduct,on_delete=models.CASCADE,related_name='green_produce_unit')
    value = models.CharField(max_length=256)
    unit = models.CharField(max_length=64)

class GreenProduceGrade(models.Model):
    unit = models.ForeignKey(GreenProduceUnit,on_delete=models.CASCADE)
    grade = models.CharField(max_length=8)
    description = models.CharField(max_length=512)
    price = models.ForeignKey(GreenProducePrice,on_delete=models.DO_NOTHING,related_name='green_produce_price')

class MeatProduct(models.Model):
    pass

class MeatUnit(models.Model):
    pass

