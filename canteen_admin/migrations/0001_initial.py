# Generated by Django 5.0.1 on 2024-02-20 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_category', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('food_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('food_subcategory', models.CharField(max_length=50)),
                ('food_desc', models.TextField()),
                ('food_image', models.ImageField(upload_to='items/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('food_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='canteen_admin.category')),
            ],
        ),
    ]
