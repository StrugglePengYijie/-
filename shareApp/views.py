from re import U
from django.shortcuts import render,redirect
from shareApp import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
# 首页
def index(request):
    articles = models.article.objects.all()
    lists = Paginator(articles,8)
    pages = request.GET.get('page')
    try:
        cons = lists.page(pages)
    except EmptyPage:
        cons = lists.page(lists.num_pages)
    except PageNotAnInteger:
        cons = lists.page(1)
    return render(request,'index.html',locals())
# 文章及留言
def article(request,id):
    if request.method == 'POST':
        name = request.POST.get('username')  
        com  = request.POST.get('coment')
        # pid = request.POST.get('pid')
        # 获取网页提交的数据
        if com == "":
            msg='留言不能为空！'
        else:
            artc = models.article.objects.get(id=id)
            comm = models.coments(name=name,com=com,To=artc,)
           
            comm.save()
            # 创建comm对象并装入数据保存
            return render(request,'article.html',locals())  
    artc = models.article.objects.get(id=id)
    return render(request,'article.html',locals())
    
# 用户登录
def logins(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        # 用authenticate判断用户名密码是否正确
        if user:
            login(request,user)
            return redirect('/shareApp/index/')
        
        else:
            msg='用户名密码错误！'
            return render(request,'login.html',locals())
    return render(request,'login.html')
    
# 用户注册
def regist(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        if password != password2 :
            msg='两次输入的密码不一样！'
            return render(request,'regist.html',locals())
        elif username == '':
            msg='用户名不能为空'
            return render(request,'regist.html',locals())
        exists = User.objects.filter(username=username).exists()
        if exists:
            msg = '该账号已注册'
            return render(request,'regist.html',locals())
        cuser = User.objects.create_user(username=username,password=password,email=email)
        cuser.save()
        return redirect('/shareApp/login/')
    return render(request,'regist.html')
# 登出
def log_out(request):
    logout(request)
    return redirect('/shareApp/index')