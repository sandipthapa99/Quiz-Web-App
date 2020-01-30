from django.db import models

# Create your models here.

class Resource(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	file = models.FileField(upload_to="resources")

	def __str__(self):
		return self.title