'''
登录和注册表单前端接口
@Autor:Thomson
Date:2018-11-08
'''

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout #用户认证
from account.forms import LoginForm,RegistrationForm


# Create your views here.

def user_login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,'login.html',{"form":login_form})
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            print(user)
            if user:
                login(request,user)
                return render(request,'about.html',{'user':cd['username']})
            else:
                return HttpResponse('抱歉，你的账号或者密码错误！')

        else:
            #报出错误
            return HttpResponse(login_form.errors)


def user_logout(request):
       logout(request)
       return render(request,'logout.html')

def register(request):
     if request.method == "POST":
          user_form = RegistrationForm(request.POST)
          if  user_form.is_valid():  #表单没有错误
              new_user = user_form.save(commit=False)
              new_user.set_password(user_form.cleaned_data['password'])
              new_user.save()
              return HttpResponse('注册成功！')
          else:
              #报出错误
              return  HttpResponse(user_form.errors)


     else:
        user_form = RegistrationForm()
        return render(request,"register.html",{"form":user_form})


