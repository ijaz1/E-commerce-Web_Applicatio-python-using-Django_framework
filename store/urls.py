from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.fnstore,name='store'),
    path('cart/',views.fncart,name='cart'),
    path('checkout/',views.fncheckout,name='checkout'),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',views.processOrder,name='process_order')
]
