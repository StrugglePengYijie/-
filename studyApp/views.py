from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import study
# Create your views here.

def studies(request,studyName):
    
    submenu = studyName
    if studyName == 'python':
        studyName = 'python'
    # elif studyName == 'linux':
    #     studyName = 'linux'
    else:
        studyName = 'linux'

    studylist = study.objects.all().filter(studyType = studyName).order_by('-publishDate')

    p = Paginator(studylist, 2)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        studylist = p.page(page)
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
        request,'studyList.html',{
            'active_menu' :'study',
            'sub_menu': submenu,
            'studyName':studyName,
            'studylist':studylist,
            'pageData': pageData,
        }
    )

def studyDetail(request, id):
   study1 = get_object_or_404(study,id = id)
   study1.views += 1
   study1.save()
   return render(request, 'studyDetail.html', {
        'active_menu': 'study',
        'study1': study1,
    })

