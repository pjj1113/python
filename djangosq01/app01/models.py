from django.db import models

# Create your models here.
class UserIfor(models.Model):
    #用户名
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)