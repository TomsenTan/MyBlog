# -*- coding:UTF-8 -*-
from django.db import models
from datetime import datetime
from slugify import slugify


class Robotkiller(models.Model):
    id = models.IntegerField(primary_key=True)  # id可以不添加，会自动创建
    rbip = models.CharField(max_length=16,default=None)
    rbvisitcount = models.IntegerField(default=0)
    rbmintimecount = models.IntegerField(default=0)
    time = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'robotkiller'








