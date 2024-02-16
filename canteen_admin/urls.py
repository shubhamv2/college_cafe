from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('adduser/',views.addUser, name='adduser'),
    path('manageusers/', views.manageUsers, name='manageusers'),
    path('addcategory/',views.addCategory, name='addcategory'),
    path('managecategories/',views.manageCategories, name='managecategories'),
    path('addfood', views.addFood, name='addfood'),
    path('managefoods', views.manageFoods, name='managefoods'),
    path('reports/', views.reports, name='reports'),
    path('reports/<int:id>/', views.deleteReport, name='deletereport'),
    path('manageusers/deleteuser/<int:id>/',views.deleteUser, name='deleteuser'),
    path('managecategories/deletecateogry/<int:id>/',views.deleteCategory, name='deletecategory'),
    path('managefoods/deletefood/<int:id>/',views.deleteFoodItem, name='deletefooditem'),
    path('manageusers/edituser/<int:id>/',views.editUser, name="edituser"),
    path('managefoods/editfood/<int:id>/',views.editFood,name='editfood'),
    path('orders/',views.orders, name='orders'),
   
]