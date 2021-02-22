from django.urls import path
from . import views

app_name = 'chinesseRestaurant'
urlpatterns = [
    path('foods/', views.ItemListView.as_view(), name='item_list')
]
