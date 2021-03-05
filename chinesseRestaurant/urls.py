from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = 'chinesseRestaurant'

urlpatterns = [
    path('', views.covidWarning, name='covidWarning'),
    re_path(r'^home/$', views.home, name='home'),
    path('customerView/', views.customerView, name='customerView'),
    #path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('foods/', views.item_list, name='item_list'),
    path('<slug:category_slug>/', views.item_list,
         name='item_list'),
    path('home/orderNow/', views.order_now, name='order_now'),
    path('customerView/edit/', views.edit, name='edit'),
    path('menu', views.menu, name='menu'),

]
