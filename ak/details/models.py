from django.db import models

# Create your models here.
class Detail(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=10)
	email = models.EmailField()

	def __str__(self):
		return self.name

