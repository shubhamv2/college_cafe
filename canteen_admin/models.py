from django.db import models

# Create your models here.
class Category(models.Model):
    food_category = models.CharField(max_length=100, null=False, blank=False, unique=True)
    def __str__(self):
        return self.food_category

class FoodItem(models.Model):
    food_name = models.CharField(max_length = 50, null=False, blank=False)
    food_category = models.ForeignKey(Category, related_name = 'category', on_delete = models.CASCADE)
    food_price = models.DecimalField(max_digits=10,decimal_places = 2, null=False, blank=False)
    food_subcategory = models.CharField(max_length=50)
    food_desc = models.TextField(null=False, blank=False)
    food_image = models.ImageField(upload_to='items/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.food_name