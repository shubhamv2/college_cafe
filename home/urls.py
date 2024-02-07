from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('menu/<str:category_name>/',views.menu, name='menu'),
    path('cart/',views.cartPage, name='cart'),
    path('add_to_cart/<int:item_id>/',views.add_to_cart, name="add_to_cart"),
    path('remove_from_cart/<int:item_id>/',views.remove_from_cart, name="remove_from_cart")
]