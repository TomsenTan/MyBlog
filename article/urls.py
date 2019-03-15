from django.conf.urls import url
from .views import *

urlpatterns = [
    url('hot_articles/', hot_articles_views),     # 热点文章列表页
    url('add_article/', add_article_views),
    # url('get_addr/', get_addr_views),
    url('get_article/', get_article_views),
    url('update_article/', update_article_views),
    url('add_article_comment', add_article_comment_views),
    url('article_modulse_python/', article_modulse_python_views),   # python文章模块
]

