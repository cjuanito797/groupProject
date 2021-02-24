from django.urls import path
from . import views

app_name = 'chinesseRestaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('foods/', views.item_list, name='item_list'),
    path('<slug:category_slug>/', views.item_list,
         name='item_list'),

]
