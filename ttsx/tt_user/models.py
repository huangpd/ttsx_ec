from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=40)
    uaddr = models.CharField(default='',max_length=100)
    uphone = models.CharField(default='',max_length=11)
    umail = models.CharField(max_length=20)
    ucode = models.CharField(default='',max_length=6)
    ushou = models.CharField(default='',max_length=10)

    def __str__(self):
        return self.uname