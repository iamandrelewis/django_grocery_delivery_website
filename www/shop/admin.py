from django.contrib import admin
from . import models as m
# Register your models here.
admin.site.register(m.Product)
admin.site.register(m.ProductCategorie)
admin.site.register(m.Price)
admin.site.register(m.ProductVarietie)
admin.site.register(m.ProductImage)
admin.site.register(m.ProductUnit)
admin.site.register(m.ProductSubCategorie)
admin.site.register(m.ProductGrade)