from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class ProcessingNode(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateField(auto_now=True, verbose_name="Date")
    description = models.TextField(blank=True)
    gpx = models.FileField(upload_to='gpx/%Y/%m/%D/', null=True)
    pollution = models.FileField(upload_to='pollution/%Y/%m/%D/', null=True)
    
    def __unicode__(self):
        return "{0} [{1}, {2}, {3}, {4}]".format(self.name, self.time, self.description, self.gpx, self.pollution)
