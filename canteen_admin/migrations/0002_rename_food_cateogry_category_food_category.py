# Generated by Django 5.0.1 on 2024-02-06 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canteen_admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='food_cateogry',
            new_name='food_category',
        ),
    ]
