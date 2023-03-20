from django.db import models

# Create your models here.
class	Info(models.Model):
	fname = models.TextField(max_length=100)
	lname = models.TextField(max_length=100)
