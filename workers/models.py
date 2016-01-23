from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Worker(models.Model):


	last_name =  models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)

	def __str__(self):

		return self.first_name +' '+ self.last_name