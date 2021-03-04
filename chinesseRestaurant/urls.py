from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'chinesseRestaurant'

urlpatterns = [
    path('', views.covidWarning, name='covidWarning'),
    path('customerView/', views.customerView, name='customerView'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('foods/', views.item_list, name='item_list'),
    path('<slug:category_slug>/', views.item_list,
         name='item_list'),
    path('order_now/', views.order_now, name='order_now'),

]
