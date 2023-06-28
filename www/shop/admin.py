from django.contrib import admin
from . import models as m
# Register your models here.
admin.site.register(m.GreenProduceProduct)
admin.site.register(m.GreenProduceProductCategorie)
admin.site.register(m.GreenProducePrice)
admin.site.register(m.GreenProduceVarietie)
admin.site.register(m.GreenProduceProductImage)
admin.site.register(m.GreenProduceUnit)
admin.site.register(m.GreenProduceGrade)