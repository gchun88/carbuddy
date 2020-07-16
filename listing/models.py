from django.db import models
import uuid

# Create your models here.

class Car(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular car')
	model_name=models.CharField(max_length=200)
	brand=models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
	launch_year=models.CharField(max_length=4)

	def __str__(self):
		return self.model_name

class CarInstance(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular car')
	car=models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
	avail_city=models.CharField(max_length=200)
	avail_state=models.CharField(max_length=2)
	price=models.CharField(max_length=200)

	def __str__(self):
		return f'{self.car.model_name}'

class Brand(models.Model):
	name=models.CharField(max_length=200)

	def __str__(self):
		return self.name