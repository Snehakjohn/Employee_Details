from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employe(models.Model):
	name = models.CharField(max_length=150)
	image = models.ImageField(null=True,blank=True, upload_to="media" )
	email = models.CharField(max_length=150)
	password = models.CharField(max_length=150)	
	phone = models.IntegerField()
	address = models.CharField(null=True,max_length=250)
	remarks = models.CharField(max_length=150)

	def _str_(self):
		return self.name