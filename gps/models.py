from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __unicode__(self):
        return "{0} [{1}]".format(self.name, self.description)

class Flight(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    time = models.DateField(auto_now=True, verbose_name="Date")
    description = models.TextField(blank=True)
    xml_file = models.FileField(upload_to='xml/', null=True) 
    def __unicode__(self):
        return "{0} [{1}, {2}, {3}]".format(self.name, self.time, self.description, self.xml_file)

class Point(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    time = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    c02 = models.IntegerField()
    nox = models.IntegerField()
    nh3 = models.IntegerField()
    def __unicode__(self):
        return "{0} [{1}, {2}, {3}, {4}, {5}, {6}]".format(self.flight, self.time, self.lat, self.lon, self.c02, self.nox, self.nh3)
    