from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class ProcessingNode(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateField(auto_now=True, verbose_name="Date")
    description = models.TextField(blank=True)
    xml_file = models.FileField(upload_to='xml/', null=True)
    
    def __unicode__(self):
        return "{0} [{1}, {2}, {3}]".format(self.name, self.time, self.description, self.xml_file)
