from django.db import models

# Create your models here.

class Car(models.Model):
	model=models.CharField(max_length=200)
	brand=models.CharField(max_length=200)
	year=models.CharField(max_length=4)

	def __str__(self):
		return self.model

class Brand(models.Model):
	name=models.CharField(max_length=200)

	def __str__(self):
		return self.name