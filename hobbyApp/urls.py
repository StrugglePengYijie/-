from django.urls import path
from . import views

app_name = 'hobbyApp'
urlpatterns = [
    path('cartoon', views.cartoon,name='cartoon'),
    path('novel', views.novel,name='novel'),
]