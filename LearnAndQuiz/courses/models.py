from django.db import models

class Course(models.Model):
	title = models.CharField(max_length=100)
	detail = models.CharField(max_length=1000, default = None)
	image= models.ImageField(upload_to="courses/images", default = None) #uploads inside base DIR(i.e media)


	def __str__(self):
		return self.title

