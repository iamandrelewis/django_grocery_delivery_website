from django.urls import path
from . import views as v

urlpatterns = [
    path('api/',v.api,name='api')
]