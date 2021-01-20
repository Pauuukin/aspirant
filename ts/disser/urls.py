from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page_url'),
    path('calculate/', calculate_page, name='calculate_page_url'),
    path('manufacturer_add/', ManufacturerAddView.as_view(), name='manufacturer_add_url')
]