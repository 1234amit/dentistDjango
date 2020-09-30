from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.Contact, name="contact"),
    path('about/', views.About, name="about"),
    path('service/', views.Service, name="service"),
    path('pricing/', views.Pricing, name="pricing"),
]