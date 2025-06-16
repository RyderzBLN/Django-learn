from django.db import models

# Create your models here.
class Gadget_List(models.Model):
    name = models.CharField(max_length=255)
    headquarters = models.CharField(max_length=255)
    founded = models.IntegerField()
    website = models.URLField()
    description = models.TextField()