from __future__ import unicode_literals

from django.db import models

# Create your models here.
class People(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{0}-{1}".format(self.id, self.name)

class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    education = models.CharField(max_length=100)
    people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.education, self.people.name)
