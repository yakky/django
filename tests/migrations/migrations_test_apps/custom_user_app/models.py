from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class MyUser(AbstractBaseUser):
    email = models.EmailField('E-Mail', unique=True)

    USERNAME_FIELD = 'email'