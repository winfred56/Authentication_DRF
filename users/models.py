from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, first_name, last_name, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned is_staff=True status')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned is_superuser=True status')
        return self.create_user(email, user_name, password, first_name, last_name, **other_fields)

    def create_user(self, email, user_name, password, first_name, last_name):
        if not email:
            return ValueError('You must enter an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, password=password, first_name=first_name,
                          last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class UserManger(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, required=True)
    user_name = models.CharField(max_length=100, required=True)
    first_name = models.CharField(max_length=100, required=True)
    last_name = models.CharField(max_length=150, required=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    def ___str__(self):
        return self.user_name