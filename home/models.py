from django.db import models
from accounts.models import User
from canteen_admin.models import FoodItem
# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem, through='CartItem')

    def __str__(self):
        return self.user.email

class CartItem(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.cart.user.email +" " +str(self.quantity)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.TextField(blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add = True)

class Report(models.Model):
    user_name = models.CharField(max_length = 50, blank=False, null=False)
    user_phone = models.CharField(max_length = 10, blank=False, null=False)
    user_email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add = True)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places = 2)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length = 50, blank=False, null=False)
    city_name = models.CharField(max_length=50, blank=False, null=False)
    state_name = models.CharField(max_length=50,blank=False, null=False)
    pin_code = models.CharField(max_length=10,blank=False, null=False)
    phone_number = models.CharField(max_length=10, blank=False, null=False)
    is_paid = models.BooleanField(default=False)
    address = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Order ${self.id}"
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OrderItem {self.id} - {self.food_item.food_name}"