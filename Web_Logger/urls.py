"""Web_Logger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
    path('admin/', admin.site.urls),
    path('Records/ssdc/', views.Web_Logger.view_records_ssdc, name="Records"),
    path('Records/ssdg/', views.Web_Logger.view_records_ssdg, name="Records"),
    path('ssdc/', views.Web_Logger.save_send_data_of_college, name="utility"),
    path('ssdg/', views.Web_Logger.save_send_data_of_google, name="utility"),
    path('Records/ssdc/delete/', views.Web_Logger.delete,name="Delete"),
    path('Records/ssdg/delete/', views.Web_Logger.delete,name="Delete"),
    path('files/download/', views.Web_Logger.download,name="download files"),
]
