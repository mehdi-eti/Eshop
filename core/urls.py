from django.urls import path

from . import views

urlpatterns = [
    path('', views.coreView, name='core-html'),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
]
