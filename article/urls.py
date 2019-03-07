from django.conf.urls  import url
from .views  import *

urlpatterns = [
    # url('',index_views),
    url('show/',show_views),   #上传文件
    url('first/',first_views),
    url('second/',first_views),
    url('list/',list_views),     #文章列表页
    url('add_article/',add_article_views),
    url('get_addr',get_addr_views),
    url('get_article/',get_article_views),
    url('update_article',update_article_views),
]

