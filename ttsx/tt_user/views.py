# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, response
from .models import *
from hashlib import sha1
import datetime


# Create your views here.

def register(request):
    context = {'title': '注册'}
    return render(request, 'tt_user/register.html', context)


def register_handle(request):
    # 接收数据
    dict = request.POST
    uame = dict.get('user_name')
    upwd = dict.get('user_pwd')
    uemail = dict.get('user_email')
    # sha1加密密码
    s1 = sha1()
    s1.update(upwd.encode("utf-8"))
    upwd_sha1 = s1.hexdigest()
    # 创建对象
    users = UserInfo()
    users.uname = uame
    users.upwd = upwd_sha1
    users.umail = uemail
    users.save()
    return redirect('/user/login/')


def register_yz(request):
    uname = request.GET.get('uname')
    result = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'valid': result})


def login(request):
    context = {'title': '登录'}
    return render(request, 'tt_user/login.html', context)


def login_handle(request):
    post = request.POST
    uname1 = post.get('username')
    upwd1 = post.get('userpwd')
    uname_jz = post.get('userjz')
    s1 = sha1()
    s1.update(upwd1.encode("utf-8"))
    upwd_sha1 = s1.hexdigest()
    context = {'title': '登录', 'username': uname1, 'userpwd': upwd1}
    result = UserInfo.objects.filter(uname=uname1)
    if result == uname1:
        context['pwd_error'] = '1'
        return render(request, 'tt_user/login.html', context)
    else:
        if result[0].upwd == upwd_sha1:
            request.session['uid'] = result[0].id
            response = redirect('/user/user_center/')
            if uname_jz == '1':
                response.set_cookie('username', uname1, expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response
        else:
            context['pwd_error'] = '1'
            return render(request, 'tt_user/login.html', context)


def user_center(request):
    return render(request, 'tt_user/user_center.html')


def user_order(request):
    return render(request, 'tt_user/user_order.html')


def user_site(request):
    return render(request, 'tt_user/user_site.html')
