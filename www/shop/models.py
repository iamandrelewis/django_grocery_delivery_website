from django.db import models
from .utils import generate_product_id


class ProductCategorie(models.Model):
    name = models.CharField(max_length=256)

class ProductSubCategorie(models.Model):
    category = models.ForeignKey(ProductCategorie,on_delete=models.CASCADE,related_name='sub_catrgory')
    name = models.CharField(max_length=256)

class Price(models.Model):
    category = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
    currency = models.CharField(max_length=256)

class Product(models.Model):
    id  = models.SlugField(primary_key=True,default=generate_product_id)
    name = models.CharField(max_length=256)
    category = models.ForeignKey(ProductCategorie,on_delete=models.CASCADE,related_name='category')
    subcategory = models.ForeignKey(ProductSubCategorie,on_delete=models.CASCADE,related_name='subcategory')

class ProductImage(models.Model):
    green_produce_product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='image')
    image = models.ImageField(upload_to='products/')

class ProductVarietie(models.Model):
    green_produce_product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='variety')
    name = models.CharField(max_length=256)
    
class ProductUnit(models.Model):
    green_produce_product= models.ForeignKey(Product,on_delete=models.CASCADE,related_name='unit')
    value = models.CharField(max_length=256)
    unit = models.CharField(max_length=64)

class ProductGrade(models.Model):
    unit = models.ForeignKey(ProductUnit,on_delete=models.CASCADE)
    grade = models.CharField(max_length=8)
    description = models.CharField(max_length=512)
    price = models.ForeignKey(Price,on_delete=models.DO_NOTHING,related_name='price')

