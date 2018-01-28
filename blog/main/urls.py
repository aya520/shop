from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('latestnews/', views.latestnews, name='latestnews'),
    path('discount/', views.discount, name='discount'),
    path('recommend/', views.recommend, name='recommend'),
    path('explain/', views.explain, name='explain'),
]