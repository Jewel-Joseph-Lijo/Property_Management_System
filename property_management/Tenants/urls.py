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
    path('user_property_list/', views.user_property_list,name='User Property List'),
    path('user_property_detail/<pk>', views.user_property_detail,name='User Property Detail'),
    path('apply_property/<pk>', views.apply_property,name='Apply Property'),
    path('applications/', views.applications,name='Applications'),
    path('my_rentals/',views.my_rentals,name='My Rentals'),
    path('my_rental_detail/',views.my_rental_detail,name='My Rental Detail'),
    path('tenant_info/<pk>',views.tenant_info,name='Tenant Info'),
    path('reject_application/<pk>',views.reject_application,name='Reject Application'),
    path('approve_application/<pk>',views.approve_application,name='Approve Application')
]