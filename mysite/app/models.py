from django.db import models

# Create your models here.


class Info(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)