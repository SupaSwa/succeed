from django.db import models

# Create your models here.

class Data(models.Model):

    original_data = models.CharField(max_length=1000)

    service_id = models.CharField(max_length=100)

    event_time = models.CharField(max_length=100)

    device_id = models.CharField(max_length=100)

    Temperature = models.IntegerField(null=True, blank=True)