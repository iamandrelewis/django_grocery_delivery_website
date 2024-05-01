from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.orders,name='orderpage'),
    path('activity',v.activity,name='orders-activity'),
    path('activity/details',v.activity_details,name='orders-activity-details'),
    path('recurring',v.recurring,name='recurring-orders'),
    path('recurring/add',v.recurring_add,name='recurring-orders-add'),
    path('recurring/details',v.recurring_details,name='recurring-orders-details'),
    path('refunds',v.refunds,name='order-refunds'),
    path('pending',v.pending,name='pending-orders'),
    path('reports',v.delivery_map,name='delivery-map'),
    path('update-recurring/',v.recurring_update, name='recurring-orders-update'),

]