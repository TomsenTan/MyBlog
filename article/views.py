from django.shortcuts import render,redirect,HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
import json
from datetime import datetime
import time
from mongoengine import Q
from article.models import Article
import printlog
from MGengine import MongoEngine as MGeng



'''
数据库基于Mongodb
'''
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
        return render(request, 'addArticle.html')
    else:
        try:
            articleAuthor = request.POST['author']
            articleTitle = request.POST['title']
            articleComment = request.POST['content']
            articleColumn = request.POST['column']
            if articleAuthor and articleTitle and articleComment and articleColumn:
                article = Article(article_author=articleAuthor, article_title=articleTitle,
                                  article_column=articleColumn, article_comment=articleComment,
                                  article_views_count=0, article_update_time=datetime.now())
            # article.switch_collection('article_more') # 切换集合，此用法需谨慎

                article.save()

        # with switch_collection(Article,'article_more') as Article_More:
        #   article = Article_More(name='Thomson', title='Phone Development', comment='python进阶教程')#切换集合
        #   article.save()
            sussOrFail = 200
            return render(request, 'addArticle.html', status=sussOrFail)

        except Exception as e:
            sussOrFail = 404
            printlog.err(e)
            return render(request, 'addArticle.html', status=sussOrFail)

        # finally:
        #     return render(request, 'articlelist.html')


# 获取文章内容
def get_article_views(request):
    if request.method == 'GET':
        # 排除掉comment字段
        # articles = Article.objects.exclude('comment').batch_size(1)
        # articles = Article.objects.exclude('views').batch_size(1)

        # 求平均阅读数
        # articles_views_average = articles.average('views')
        # print(articles_views_average)

        # articles = MGeng(Article).GETAll()
        _key = 'article_views_count'
        articles = MGeng(Article).ORDER(_key, des=-1)
        return render(request, 'articlelist.html', locals())
    else:
        INFO = 'get article'
        printlog.info(INFO)


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
            INFO = 'update article'
            printlog.info(INFO)


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
