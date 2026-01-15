"""
URL configuration for property_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('company_home/', views.company_home,name='Company Home'),
    path('add_property/', views.add_property,name='Add Property'),
    path('property_list/', views.property_list,name='Property List'),
    path('property_detail/<pk>', views.property_detail,name='Property Detail'),
    path('edit_property/<pk>', views.edit_property,name='Edit Property'),
    path('delete_property/<pk>', views.delete_property,name='Delete Property')
]