from django.urls import path
from . import views

app_name = 'chinesseRestaurant'

urlpatterns = [
    path('', views.covidWarning, name='covidWarning'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('foods/', views.item_list, name='item_list'),
    path('<slug:category_slug>/', views.item_list,
         name='item_list'),
    path('order_now/', views.order_now, name='order_now'),

]
