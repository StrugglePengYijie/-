from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import line
# Create your views here.
def lines(request,lineName):
    submenu = lineName
    if lineName == 'cartoonsaying':
        lineName = '动漫语录'
    elif lineName == 'booksaying':
        lineName = '书籍名句'
    else:
        lineName = '小说摘抄'

    lineList = line.objects.all().filter(lineType = lineName).order_by('-publishDate')

    p = Paginator(lineList, 2)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        lineList = p.page(page)
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

    return render(
        request,'lineList.html',{
            'active_menu' :'line',
            'sub_menu': submenu,
            'lineName':lineName,
            'lineList':lineList,
            'pageData': pageData,
        }
    )

def lineDetail(request, id):
    lines = get_object_or_404(line,id = id)
    lines.views += 1
    lines.save()
    return render(request, 'lineDetail.html', {
        'active_menu': 'line',
        'line': lines,
    })