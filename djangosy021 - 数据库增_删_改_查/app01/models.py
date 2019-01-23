from django.db import models

# Create your models here.
class UserGroup(models.Model):
    uid =models.AutoField(primary_key=type)
    caption = models.CharField(max_length=32)


class UserInfo(models.Model):
    #用户名列,字符串类型
    username =models.CharField(max_length=32)
    password = models.CharField(max_length=64)