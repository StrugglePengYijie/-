from django.shortcuts import render
from django.shortcuts import HttpResponse
from anecodoteApp.models import anecodote
from django.db.models import Q
from hobbyApp.models import Cartoon
from lineApp.models import line
from shareApp.models import article
from studyApp.models import study
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
@cache_page(60 * 15) # 单位：秒数，这里指缓存 15 分钟
def home(request):
    # 新闻展报
    anecodoteList = anecodote.objects.all().filter(~Q(
        anecodoteType='附近趣事')).order_by('-publishDate')
    postList = set()
    postNum = 0
    for s in anecodoteList:
        if s.photo:
            postList.add(s)
            postNum += 1
        if postNum == 3:  # 只截取最近的3个展报
            break

    # 新闻列表
    if (len(anecodoteList) > 11):
        anecodoteList = anecodoteList[0:11]
    # anecodoteList = anecodote.objects.all().filter(
    #     Q(anecodoteType='附近趣事')).order_by('-publishDate')
    # if (len(anecodoteList) > 4):
    #     anecodoteList = anecodoteList[0:4]
    # 通知公告
    lineList = line.objects.all().filter(
        Q(lineType='动漫语录')).order_by('-publishDate')
    if (len(lineList) > 4):
        lineList = lineList[0:4]

    # 学习中心
    studylist = study.objects.all().filter(
        Q(studyType='python')).order_by('-publishDate')
    if(len(studylist)>4):
        studylist = studylist[0:4]

    #文章中心
    articlelist = article.objects.all().order_by('-c_tim')
    if(len(articlelist)>4):
        articlelist = articlelist[0:4]
        # lists = Paginator(articlelist,8)
        # pages = request.GET.get('page')
        # try:
        #     cons = lists.page(pages)
        # except EmptyPage:
        #     cons = lists.page(lists.num_pages)
        # except PageNotAnInteger:
        #     cons = lists.page(1)
        
    cartoonlist = line.objects.all().filter(
        Q(lineType='动漫语录')).order_by('-publishDate')
    
    if(len(cartoonlist)>4):
        cartoonlist = cartoonlist[0:4]
    # 返回结果
    return render(request, 'home.html', {
        'active_menu': 'home',
        'postList': postList,
        'anecodoteList': anecodoteList,
        'lineList': lineList,
        'studylist':studylist,
        'articlelist':articlelist,
        'cartoonlist':cartoonlist,
    })