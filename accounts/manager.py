from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, name, email, phone, password):
        if not email:
            raise ValueError("Email is required. ")
        
        user = self.model(email=self.normalize_email(email), name=name, phone = phone)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, name, email, password,phone=None):
        user = self.create_user(name, email, phone, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
