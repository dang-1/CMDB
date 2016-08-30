from django.db import models

# Create your models here.
class Host(models.Model):
    '''store host information'''
    hostname = models.CharField(max_length=50)
    ip = models.IPAddressField()
    vendor = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    sn = models.CharField(max_length=50)
    cpu_model = models.CharField(max_length=50)
    cpu_num = models.IntegerField(max_length=50)
    memory = models.CharField(max_length=50)
    osver = models.CharField(max_length=50)
    def __unicode__(self):
        return self.hostname
