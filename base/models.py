#coding=utf-8
from django.db import models
from django.utils import timezone
# Create your models here.


class Bugs(models.Model):
    def __unicode__(self):
        return self.datetime
    user = models.CharField(max_length=255)
    add_date = models.DateTimeField('创建日期',auto_now=True)
    last_date = models.DateTimeField('最后修改日期',auto_now=True)
    content = models.TextField(null=True)
    img = models.ImageField(default='')
    result = models.BooleanField(default=False)