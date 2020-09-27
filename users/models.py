from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField


class tblUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = ((True, 'Male'), (False, 'Female'), (None, 'Do not want to answer'))
    permission_status = ((1, 'level 0'), (2, 'Level 1'), (3, 'Level 2'))
    email = models.EmailField(_('email address'), unique=True, error_messages={
        'unique': _("A user with that email already exists."),
    }, )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    Firstname = models.CharField(max_length=100, null=True)
    Lastname = models.CharField(max_length=100, null=True)
    Zipcode = models.IntegerField(null=True, blank=True)
    Phone = PhoneNumberField(null=True, blank=True)
    Gender = models.BooleanField(default=None, null=True, choices=GENDER_CHOICES, blank=True)
    permission_status = models.IntegerField(default=2, null=False, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Firstname', 'Lastname']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
