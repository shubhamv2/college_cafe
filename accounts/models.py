from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
# Create your models here.


class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length = 100, blank = False, null = False)
    email = models.EmailField(blank = False, null = False, unique=True)
    phone = models.CharField(max_length = 13, blank = True, unique=True)
    profile_img = models.ImageField(upload_to='profiles/')
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    join_date = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']
    objects = UserManager()

    def __str__(self) -> str:
        return self.email

