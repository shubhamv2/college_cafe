from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Report)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)