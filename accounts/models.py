from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True,  validators=[RegexValidator(r'^998(9[012345789]|6[125679]|7[01234569])[0-9]{7}$')])
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

