from django.db import models

# Create your models here.
class User(models.Model):
    id= models.CharField(max_length=255, unique=True, primary_key=True)
    real_name = models.CharField(max_length=255)
    tz = models.CharField(max_length=255)

class ActivityPeriod(models.Model):
    userId = models.ForeignKey('User', on_delete=models.CASCADE)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)