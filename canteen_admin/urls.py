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
    path('report', views.reports, name='reports'),
    path('manageusers/deleteuser/<int:id>/',views.deleteUser, name='deleteuser'),
    path('managecategories/deletecateogry/<int:id>/',views.deleteCategory, name='deletecategory'),
    path('managefoods/deletefood/<int:id>/',views.deleteFoodItem, name='deletefooditem'),
    path('manageusers/edituser/<int:id>/',views.editUser, name="edituser"),
    path('orders/pending_orders/',views.pendingOrders, name='pendingorders'),
    path('orders/delivered_orders/',views.deliveredOrders, name='deliveredorders')
]