from django.urls import path
from . import views as v
urlpatterns = [
    path('',v.shop,name='shoppage'),

    path('green-produce', v.green_produce, name='green_produce-main'),
    path('green-produce/all',v.green_produce_all,name='green_produce-all'),
    path('green-produce/fruits',v.green_produce_fruits,name='green_produce-fruits'),
    path('green-produce/vegetables',v.green_produce_vegetables,name='green_produce-vegetables'),
    path('green-produce/herbs-spices',v.green_produce_herbs_spices,name='green_produce-herbs-spices'),
    path('green-produce/tubers-provisions',v.green_produce_tubers_provisions,name='green_produce-tubers-provisions'),
    path('green-produce/nuts-grains',v.green_produce_nuts_grains,name='green_produce-nuts-grains'),
    path('products/details',v.product_details,name='product-details'),


    path('meats',v.meats,name='meats-main'),
    path('meats/all',v.meats_all,name='meats-all'),
    path('meats/poultry',v.meats_poultry,name='meats-poultry'),
    path('meats/lean',v.meats_lean,name='meats-lean'),
    path('meats/fish-seafood',v.meats_fish_seafood,name='meats-fish-seafood'),
    path('meats/deli',v.meats_deli,name='meats-deli'),

    path('deals',v.deals,name='deals'),
    path('buy-it-again',v.buy_it_again,name='buy-it-again'),

]   