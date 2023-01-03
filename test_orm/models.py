from django.db import models
from django.contrib.auth.models import User


class Entity(models.Model):
    modified_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    value = models.IntegerField()
    properties = models.ManyToManyField('Property', related_name='property')


class Property(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.key