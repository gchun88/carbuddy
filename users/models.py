from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField

class tblUser(AbstractUser):
    GENDER_CHOICES = ((True,'Male'),(False,'Female'),(None,'Do not want to answer'))
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    Firstname = models.CharField(max_length=100,null=True)
    Lastname = models.CharField(max_length=100,null=True)
    Zipcode = models.IntegerField(max_length=20,null=True)
    Phone = PhoneNumberField(null=True)
    Gender = models.BooleanField(default=None,null=True,choices=GENDER_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Firstname','Lastname']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


