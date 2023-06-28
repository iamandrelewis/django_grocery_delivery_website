from django.urls import path
from . import views as v

urlpatterns = [
    path('about',v.about_us,name='about-us'),
    path('careers',v.careers,name='careers'),
    path('investors',v.investors,name='investors'),
    path('how-it-works',v.how_it_works,name='how-it-works'),
]