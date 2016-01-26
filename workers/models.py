from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Worker(models.Model):

	pp = (
		('Y','Yes'),
		('N','No'),
		)
	sx = (
		('F','Female'),
		('M','Male'),
		)

	last_name =  models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	age = models.CharField(max_length=3,default=1)
	sex = models.CharField(max_length=1,choices=sx)
	email = models.EmailField(default='s@sergioe21.com')
	paid = models.CharField(max_length=1,choices = pp)
	url_background = models.CharField(max_length=500,default='http://www.vallourec-ra2013.com/assets/img/background/background-univ-petrole-degrade.png')

	def __str__(self):

		return self.first_name +' '+ self.last_name

	def get_paid(self):

		self.paid = 'Y'
		self.save()

	def to_pay(self):

		self.paid = 'N'
		self.save()

	