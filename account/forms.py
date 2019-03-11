'''
重写登录表单
@Autor:Thomson
Date:2018-11-08
'''

from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # email = forms.CharField()


class RegistrationForm(forms.ModelForm):
    #重写密码输入框
    password = forms.CharField(label="请输入密码",widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    class Meta:  #内部类与数据库关联
        model = User
        fields = ("username","email")

    #验证两次输入的密码
    def clean_password2(self):
        cd = self.cleaned_data  #表单数据栏
        if cd['password'] != cd['password2']:
            print(cd["password"])
            print(cd["password2"])
            raise forms.ValidationError('两次输入的密码不相同')
        return cd['password2']

