from django.urls import path
from profit import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('casestudies/', views.casestudies, name='casestudies'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
]