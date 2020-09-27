from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.
#
# class tblUser(AbstractBaseUser):
#   User_ID = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#   User_name = models.CharField(max_length=20)
#   Password = models.CharField(max_length=20)
#   Active = models.IntegerField(max_length=5)
#   First_name = models.CharField(max_length=100)
#   Last_name = models.CharField(max_length=100)
#   Zipcode = models.IntegerField(max_length=20)
#   Email = models.CharField(max_length=100)
#   Phone = models.IntegerField(max_length=20)
#   Gender = models.CharField(max_length=1)
#   Registration_date = models.DateTimeField('date registered')
#   REQUIRED_FIELDS = ['']
