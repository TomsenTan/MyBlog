# -*- coding:UTF-8 -*-
from django.db import models
from mongoengine import *
from slugify import slugify
from datetime import datetime
import time


connect('blog_test')

#monogodb数据集合映射
class Article(Document):
    meta = {
        'collection': 'article'
    }
    article_id = SequenceField(required=True, primary_key=True)
    article_author = StringField(max_length=50)
    article_title = StringField(max_length=50)
    article_column = StringField(max_length=50)
    article_comment = StringField()
    # article_comment = ListField()
    article_views_count = IntField()
    article_update_time = DateTimeField(default=datetime.now())  # 注意不是DateField(否则只存日期)

    @queryset_manager
    def get_article_by_queue(doc_cls, queryset):
        return queryset.order_by('+aruticle_id')

    def __str__(self):
        return self.article_author

    def save(self, *args, **kwargs):
        self.slug = slugify(self.article_author)
        super(Article, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('article:article_detail', args=[self.article_id,self.slug])


