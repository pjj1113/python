from django.db import models

# Create your models here.
class UserGroup(models.Model):
    uid =models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    ctme = models.DateField(auto_now_add=True,null=True)
    uptime = models.DateField(auto_now=True,null=True)


class UserInfo(models.Model):
    #用户名列,字符串类型
    username =models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=60)
    test = models.EmailField(max_length=19,null=True,error_messages={'invail':'请输入密码'})
    user_group = models.ForeignKey('UserGroup',to_field='uid',default=1)
    user_type_choices = (
        (1,'超级用户'),
        (2,'普通用户'),
        (3,'普普通用户'),
    )



