from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.TextField(max_length=20)
