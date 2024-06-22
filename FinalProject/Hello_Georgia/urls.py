"""
URL configuration for FinalProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
    path('', views.home, name="Home"),
    path('about/', views.base, name="About"),
    path('add_visitor/', views.add_visitor, name='add_visitor'),
    path('Kaxeti/', views.kaxeti, name="Kaxeti"),
    path('Samegrelo/', views.samegrelo, name="Samegrelo"),
    path('Abkhazeti/', views.Abkhazeti, name="Abkhazeti"),
    path('Guria/', views.Guria, name="Guria"),
    path('Adjara/', views.Adjara, name="Adjara"),
    path('Mtskheta_Mtianeti/', views.Mtskheta_Mtianeti, name="Mtskheta_mtianeti"),
    path('Samtskhe_Javakheti/', views.Samtskhe_Javakheti, name="Samtskhe_Javakheti"),
    path('Shida_Kartli/', views.Shida_Kartli, name="Shida_Kartli"),
    path('Kvemo_Kartli/', views.Kvemo_Kartli, name="Kvemo_Kartli"),
    path('Imereti/', views.Imereti, name="Imereti"),
    path('Racha_Lechkhumi/', views.Racha_Lechkhumi, name="Racha_Lechkhumi"),

]
