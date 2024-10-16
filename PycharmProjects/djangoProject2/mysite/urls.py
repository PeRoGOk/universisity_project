from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ficha/', views.ficha, name='ficha'),
    path('calculator/', views.calculator, name='calculator'),
]
