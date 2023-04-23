from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy

class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('You need Email address!')
        user = self.model(
            email = email,
            date_of_birth = date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,date_of_birth,password=None):
        user = self.model(
            email = email,
            date_of_birth = date_of_birth,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class MyUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
    
    objects = UserManager()
    
    def get_absolute_url(self):
        return reverse_lazy('useraccount:top')
