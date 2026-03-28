from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_store/', views.chai_store, name='chai_store')
    # path('order/', views.order_chai, name='orderchai'),
    # path('latte/', views.lattechoices, name='lattechoices'),
    
]
