from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('chapa/', views.chapa_webhook,name='chapa_webhook')
]
