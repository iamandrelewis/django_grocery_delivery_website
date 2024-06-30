from django.db import models
from .utils import generate_product_id

"""
"""

class ProductCategorie(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return f"{self.name}"

class ProductSubCategorie(models.Model):
    category = models.ForeignKey(ProductCategorie,on_delete=models.CASCADE,related_name='sub_catrgory')
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.category.name}:{self.name}"

class Price(models.Model):
    category = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
    currency = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"${self.value} {self.currency}"
    
class Product(models.Model):
    id  = models.SlugField(primary_key=True,default=generate_product_id)
    name = models.CharField(max_length=256)
    subcategory = models.ForeignKey(ProductSubCategorie,on_delete=models.CASCADE,related_name='subcategory')

    def __str__(self) -> str:
        return f"{self.name}"

class ProductVarietie(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='variety')
    name = models.CharField(max_length=256)
    def __str__(self) -> str:
        return f"{self.pk} {self.name} {self.product.name} "

class ProductImage(models.Model):
    product = models.ForeignKey(ProductVarietie,on_delete=models.CASCADE,related_name='image')
    image = models.ImageField(upload_to='products/')

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class ProductUnit(models.Model):
    product= models.ForeignKey(ProductVarietie,on_delete=models.CASCADE,related_name='unit')
    value = models.CharField(max_length=256)
    unit = models.CharField(max_length=64)
    unit_abbr = models.CharField(max_length=64,default='lb')
    def __str__(self) -> str:
        return f"per {self.unit} ({self.unit_abbr})"

class ProductGrade(models.Model):
    product = models.ForeignKey(ProductVarietie,on_delete=models.CASCADE)
    unit = models.ForeignKey(ProductUnit,on_delete=models.CASCADE)
    grade = models.CharField(max_length=8)
    description = models.CharField(max_length=512)
    price = models.ForeignKey(Price,on_delete=models.DO_NOTHING,related_name='price')
    cost_price = models.CharField(max_length=265,null=True,blank=True)
    cost_price_currency = models.CharField(max_length=256,null=True,blank=True)
    selling_price = models.CharField(max_length=265,null=True,blank=True)
    selling_price_currency = models.CharField(max_length=265,null=True,blank=True)
    is_taxable = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk}-{self.product}: Grade {self.grade} @ ${self.price.value} {self.price.currency}/{self.unit.unit_abbr    }"


class ProductDeal(models.Model):
    product = models.ForeignKey(ProductGrade,on_delete= models.CASCADE)
    new_price = models.CharField(max_length=128,null=True,blank=True)
    type = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True, blank=True)
    @property
    def discount(self):
        try:
           discount =  ((self.product.price.value - self.new_price)/self.product.price.value)*100
        except:
            discount = 0
        return discount
    
class RelatedProductDealItem(models.Model):
    deal = models.ForeignKey(ProductDeal,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductGrade,on_delete=models.CASCADE)
    new_price = models.CharField(max_length=128,null=True,blank=True)
    
    @property
    def discount(self):
        try:
           discount =  ((self.product.price.value - self.new_price)/self.product.price.value)*100
        except:
            discount = 0
        return discount