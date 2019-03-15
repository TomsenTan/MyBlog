from django.db import models
from mongoengine import *


connect('blog_test')

#monogodb数据集合映射
class Article(Document):
    meta = {
        'collection': 'article_data'
    }
    article_id = SequenceField(required=True, primary_key=True)
    arctle_name = StringField(max_length=50)
    artilce_title = StringField(max_length=50)
    article_comment = ListField()
    article_views_count = IntField()

    @queryset_manager
    def get_article_by_queue(doc_cls, queryset):
        return queryset.order_by('+aruticle_id')





