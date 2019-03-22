from django.shortcuts import render
from robotkiller.models import Robotkiller
from datetime import datetime
from .configs import visit_max_count,visit_min_seconds,visit_min_seconds_count
import printlog

def filterIP(request):
    '''
    :param request:
    :return:
        1   -- 表示可以继续返回界面
        -1  -- 表示不可以返回界面
        0   -- 表示获取不到IP
    '''
    # 主机名
    domain = request.META.get('REMOTE_HOST')
    white_list = ['googlebot.com','crawl.baidu.com','sogou.com','bing.com']  # 白名单
    for bot_domain in white_list:
        if domain and domain.find(bot_domain) > 0:
           return 1

    # 获取IP
    user_ip = request.META.get('REMOTE_ADDR')
    if not user_ip:
        printlog.err('Get user_ip fail')
        return 0

    try:
        DATAS = Robotkiller.objects.get(rbip=user_ip)
    except Robotkiller.DoesNotExist:
        Robotkiller.objects.create(rbip=user_ip, rbvisitcount=1, rbmintimecount=0)
        return 1

    # 对访问时间间隔作捕获
    now = datetime.now()
    passed_seconds = (now-DATAS.time).seconds  # 转化为秒

    # 具体逻辑可以是and/or
    if DATAS.rbvisitcount > visit_max_count or DATAS.rbmintimecount > visit_min_seconds_count:
        return -1
    else:
        if passed_seconds < visit_min_seconds:
            DATAS.rbmintimecount += 1
            DATAS.save()
            return 1
        else:
            DATAS.rbvisitcount += 1
            DATAS.time = now
            DATAS.save()
            return 1