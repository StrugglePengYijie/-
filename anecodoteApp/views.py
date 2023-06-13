from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import anecodote
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from pyquery import PyQuery as pq

def anecodotes(request,anecodoteName):
    submenu = anecodoteName  #参数
    if anecodoteName == 'nearby':
        anecodoteName = '附近趣事'
   
    else:
        anecodoteName = '网络趣闻'
    
    anecodoteList = anecodote.objects.all().filter(anecodoteType = anecodoteName).order_by('-publishDate')
    for anecodote1 in anecodoteList:
        html = pq(anecodote1.description)
        anecodote1.mytxt = pq(html)('p').text()

    p = Paginator(anecodoteList, 5)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        anecodoteList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }

    return render(request,'anecodoteList.html',{
        'active_menu':'anecodote',
        'sub_menu':submenu,
        'anecodoteName':anecodoteName,
        'anecodoteList':anecodoteList,
        'pageData':pageData,
    })

def anecodoteDetail(request,id):
    anecodote1 = get_object_or_404(anecodote,id=id)
    anecodote1.views+=1
    anecodote1.save()

    return render(request,'anecodoteDetail.html',{
        'anecodote1':anecodote1,
        'active_menu':'anecodote',
    })

def search(request):
    
    keyword = request.GET.get('keyword')
    anecodoteList = anecodote.objects.filter(title__icontains=keyword)
    anecodoteName = "关于 " + "\"" + keyword + "\"" + " 的搜索结果"    
    return render(request,'searchList.html',{
        'active_menu':'anecodote',
        'anecodoteName':anecodoteName,
        'anecodoteList':anecodoteList,
    })


