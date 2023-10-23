# Create your models here.
from django.db import models

class PCSystemInfo(models.Model):
    pc_name = models.CharField(max_length=255, unique=True)
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()
    ram_total = models.FloatField()
    ram_available = models.FloatField()
    installed_apps = models.JSONField()
    
    def __str__(self):
        return self.pc_name
