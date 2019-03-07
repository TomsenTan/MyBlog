from django.db import models
from datetime import datetime
# Create your models here.

class Robotkiller(models.Model):
    # id = models.IntegerField(primary_key=True,) 注意id可以不添加，会自动创建
    ip = models.CharField(max_length=16)
    visits = models.IntegerField()
    time = models.DateTimeField(default=datetime.now())
    class Meta:
        db_table = 'robotkiller'

