from django.shortcuts import render
from django.template import  loader
from django.http  import HttpResponse
from article.models import Article

# Create your views here.

def index_views(request):

    return render(request,'first.html')


def  show_views(request):
     # t = loader.get_template('show.html')
     # html = t.render({'title':'music'})  #不一样的东西可以传入变量，如不同的新闻内容
     # return HttpResponse(html)
     return render(request,'show.html',{'title':'music'})


def first_views(request):
    return render(request,'first.html')

def second_views(request):
     return render(request,'second.html')

def list_views(request):
    return render(request,'list.html')

#获取请求的报头进行分析
def get_addr_views(request):
    addr = request.META['REMOTE_ADDR']
    http_header = {}
    http_header['addr'] = addr
    return HttpResponse(addr)

'''
以下内容是基于Mongodb数据库的实现
Date:2018-11-09
'''

#添加文章(已添加)
def add_article_views(request):
    if request.method == "GET":
         return render(request,'add_article.html')
    else:
        try:
            name = request.POST['author']  #获取表单的内容
            title = request.POST['title']
            content = request.POST['content']
            article = Article(name=name, title=title,comment=content)
            # article.switch_collection('article_more') #切换集合，此用法需谨慎
            article.save()

        # with switch_collection(Article,'article_more') as Article_More:
        #   article = Article_More(name='Thomson', title='Phone Development', comment='python进阶教程')#切换集合
        #   article.save()


            return HttpResponse('发布成功')

        except Exception as e:
            print(e)
            return HttpResponse('发布失败')



    # return render(request,'list.html')

#获取文章内容
def get_article_views(request):
    # articles = Article.objects.exclude('comment').all_fields()
    #排除掉comment字段
    # articles = Article.objects.exclude('comment').batch_size(1)

    articles = Article.objects.exclude('views').batch_size(1)

    #求平均阅读数
    # articles_views_average = articles.average('views')
    # print(articles_views_average)

    return render(request,'demo.html',locals())

#修改文章内容(已修改)
def update_article_views(request):
    article = Article.objects.first()
    try:
        article.update(comment='请问学习web开发需要看什么书？',views=60)
        article.save()
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse('Error')

