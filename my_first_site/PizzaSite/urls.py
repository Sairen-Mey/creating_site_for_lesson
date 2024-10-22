from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('PizzaSite/', views.members, name='PizzaSite'),
    path('PizzaSite/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]