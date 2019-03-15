from django.shortcuts import render,redirect,HttpResponseRedirect
from django.template import  loader
from django.http import HttpResponse
import json
from mongoengine import Q
from article.models import Article
import printlog

'''
数据库基于Mongodb
'''


def index_views(request):
    return render(request, 'first.html')

def article_modulse_python_views(request):
     # t = loader.get_template('show.html')
     # html = t.render({'title':'music'})  # 不一样的东西可以传入变量，如不同的文章分类模块
     # return HttpResponse(html)
     return render(request, 'show.html', {'title': 'python'})


def hot_articles_views(request):
    return render(request, 'hotArticle.html')

# 获取请求的报头进行分析
# def get_addr_views(request):
#     addr = request.META['REMOTE_ADDR']
#     http_header = {}
#     http_header['addr'] = addr
#     return HttpResponse(addr)


# 添加文章
def add_article_views(request):
    if request.method == "GET":
        return render(request, 'add_article.html')
    else:
        try:
            addName = request.POST['author']
            addTitle = request.POST['title']
            addComment = request.POST['content']
            article = Article(name=addName, title=addTitle, comment=addComment)
            # article.switch_collection('article_more') # 切换集合，此用法需谨慎
            article.save()

        # with switch_collection(Article,'article_more') as Article_More:
        #   article = Article_More(name='Thomson', title='Phone Development', comment='python进阶教程')#切换集合
        #   article.save()
            sussOrFail = 200
            return render(request, 'hotArticle.html', status=sussOrFail)

        except Exception as e:
            sussOrFail = 404
            return render(request, 'add_article.html', status=sussOrFail)

        finally:
            return render(request, 'hotArticle.html')


# 获取文章内容
def get_article_views(request):
    if request.method == 'GET':
        # 排除掉comment字段
        # articles = Article.objects.exclude('comment').batch_size(1)

        articles = Article.objects.exclude('views').batch_size(1)

        # 求平均阅读数
        articles_views_average = articles.average('views')
        # print(articles_views_average)

        return render(request, 'article.html', locals())
    else:
        printlog.info()


# 修改文章内容
def update_article_views(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/article/get_article')
    else:
        try:
            article = Article.objects.first()

            postBody = request.body
            postContent = json.load(postBody)
            postComment = postContent.comment

            article.update(comment=postComment, views=60)
            article.save()
            return HttpResponse('OK')

        except Exception as e:
            printlog.err(e)

        finally:
            printlog.info()


# 添加文章评论
def add_article_comment_views(request):
    if request.method == 'POST':
        try:
            commentBody = request.body.commennt
            commentName = request.body.NAME
            commentContent = request.body.content
            if commentBody:
               Article.objects(Q(article_name=commentName))\
                    .update_one(push__article_comment=commentContent)
            else:
                err = 'No comments gets'
                printlog.err(err)

        except Exception as e:
            printlog.err(e)

        finally:
            pass
    else:
        info = 'Cannot be method GET'
        printlog.info(info)
