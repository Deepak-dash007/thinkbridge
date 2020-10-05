from django.db import models

# Create your models here.

class Inventory(models.Model):
	"""docstring for Inventory"""
	name = models.CharField(max_length=100,default='Something')
	image = models.ImageField(null=True, default='No-image-available.png')
	description = models.CharField(max_length=100, default='Describe Something')
	price = models.IntegerField( default=0)
