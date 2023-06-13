from django.urls import path
from . import views

app_name = 'anecodoteApp'
urlpatterns = [
    path('anecodotes/<str:anecodoteName>/',views.anecodotes,name='anecodotes'),
    path('anecodoteDetail/<int:id>/',views.anecodoteDetail,name='anecodoteDetail'),
    path('search/',views.search,name='search'),
]