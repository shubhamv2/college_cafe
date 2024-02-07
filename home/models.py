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


class Report(models.Model):
    user_name = models.CharField(max_length = 50)
    user_phone = models.CharField(max_length = 10)
    user_email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)