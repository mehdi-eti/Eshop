from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.eshop_login),
    path('register/', views.eshop_register),
    path('log-out',views.log_out)
]