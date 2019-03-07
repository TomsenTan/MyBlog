from django.conf.urls  import url
from .views  import *

urlpatterns = [
    url('about_me',about_views,name='about_me'),
#     url('show/',show_views)
]