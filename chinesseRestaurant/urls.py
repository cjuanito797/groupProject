from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = 'chinesseRestaurant'

urlpatterns = [
    path('', views.covidWarning, name='covidWarning'),
    re_path('home/', views.home, name='home'),
    path('customerView/', views.customerView, name='customerView'),
    # path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('foods/', views.item_list, name='item_list'),
    path('foods/<slug:category_slug>/', views.item_list,
         name='item_list'),
    path('orderNow/', views.order_now, name='order_now'),
    path('menu/', views.menu, name='menu'),
    path('edit/', views.edit, name='edit'),
    path('edit_delivery', views.editDeliveryPref, name="editDeliveryPref"),

]
