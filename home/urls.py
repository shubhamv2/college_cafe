from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('menu/<str:category_name>/',views.menu, name='menu'),
    path('review/',views.review_page,name='review'),
    path('cart/',views.cartPage, name='cart'),
    path('cart/place_order/', views.place_order, name='placeorder'),
    path('add_to_cart/<int:item_id>/',views.add_to_cart, name="add_to_cart"),
    path('remove_from_cart/<int:item_id>/',views.remove_from_cart, name="remove_from_cart"),
    path('userorders/',views.userOrders, name='userorders'),
    path('increment_item/<int:item_id>/',views.increment_item, name='increment'),
    path('decrement_item/<int:item_id>/',views.decrement_item, name='decrement'),
    path('cart/place_order/ordersuccess/',views.order_success,name="ordersuccess"),
    path('cart/place_order/payment/',views.payment, name='paymentpage'),
    path('cart/place_order/payment/makepayment',views.makePayment, name='makepayment'),

]