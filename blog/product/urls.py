from django.urls import path
from product import views


app_name = 'product'
urlpatterns = [
    path('', views.product, name='product'),
    path('a/', views.a, name='a'),
    path('b/', views.b, name='b'),
    path('c/', views.c, name='c'),
    path('d/', views.d, name='d'),
]