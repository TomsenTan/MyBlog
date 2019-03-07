from django.shortcuts import render
from robotkiller.models import Robotkiller
from datetime import datetime

# Create your views here.
max_visits = 10
min_seconds = 10

def filterIP(request):
    domain = request.META.get('REMOTE_HOST')
    white_list = ['googlebot.com','crawl.baidu.com','sogou.com','bing.com']
    for bot_domain in white_list:
        if domain.find(bot_domain)>0:  #在白名单范围内,否则自动返回None
            return bot_domain

    #对IP访问次数作捕获
    user_ip = request.META.get('REMOTE_ADDR')

    try:
        record = Robotkiller.objects.using('robotkiller').get(ip=user_ip)
    except Robotkiller.DoesNotExist:
        Robotkiller.objects.using('robotkiller').create(ip=user_ip,visits=1)
        return

    #对访问时间间隔作捕获
    passed_seconds = (datetime.now()-record.time).seconds #转化为秒
    print(passed_seconds)

    #具体逻辑可以是and/or
    if record.visits > max_visits and passed_seconds < min_seconds:
        raise Exception('user ip banned')  #发出错误
    else:
        if passed_seconds < min_seconds:
            record.visits = record.visits+1
            record.save()
        else:
            record.visits = 1
            record.time = datetime.now()
            record.save()
