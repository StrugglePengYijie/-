from django.urls import path
from django.conf.urls import url,include
from . import views

app_name = 'shareApp'
urlpatterns = [
  url(r'^index', views.index,name='index'),
  url(r'^regist/', views.regist,name='regist'),
  url(r'^login/$',views.logins, name= 'login'),
  url(r'^log_out', views.log_out,name='log_out'),
  url(r'^article/(\d+)$',views.article,name='article'),
  
]