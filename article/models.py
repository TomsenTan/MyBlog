from django.db import models
from mongoengine import *

# Create your models here.

connect('blog_test')

#monogodb数据集合映射
class Article(Document):
    name = StringField(max_length=50)
    title = StringField(max_length=50)
    comment = StringField()
    views = IntField()



