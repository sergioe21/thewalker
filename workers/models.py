from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Worker(models.Model):

	pp = (
		('Y','Yes'),
		('N','No'),
		)

	last_name =  models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)

	paid = models.CharField(max_length=1,choices = pp)

	def __str__(self):

		return self.first_name +' '+ self.last_name

	def get_paid(self):

		self.paid = 'Y'
		self.save()

	def to_pay(self):

		self.paid = 'N'
		self.save()

	