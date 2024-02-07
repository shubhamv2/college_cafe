from django.db import models

# Create your models here.
class Category(models.Model):
    food_category = models.CharField(max_length=100)
    def __str__(self):
        return self.food_category

class FoodItem(models.Model):
    food_name = models.CharField(max_length = 50)
    food_category = models.ForeignKey(Category, related_name = 'category', on_delete = models.CASCADE)
    food_price = models.IntegerField()
    food_desc = models.TextField()
    food_image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.food_name