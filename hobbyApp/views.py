from django.shortcuts import render
from . models import Cartoon

# Create your views here.
def cartoon(request):
    cartoons = Cartoon.objects.all()
    return render(request,'cartoon.html',{'active_menu':'hobby',
                                        'sub_menu':'cartoon',
                                        'cartoons':cartoons,})

def novel(request):
    return render(request,'novel.html',{'active_menu':'hobby','sub_menu':'novel',})