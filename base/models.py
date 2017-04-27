#coding=utf-8
from django.db import models
from django.utils import timezone
# Create your models here.


class Bugs(models.Model):
    def __unicode__(self):
        return self.user
    user = models.CharField('用户',max_length=255)
    projectName = models.CharField('项目名称',max_length=255)
    add_date = models.DateTimeField('创建日期',auto_now=True)
    last_date = models.DateTimeField('最后修改日期',auto_now=True)
    content = models.TextField('Bug内容',null=True)
    img = models.ImageField('图片',default='')
    result = models.BooleanField('处理情况',default=False)