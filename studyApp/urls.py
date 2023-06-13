from django.urls import path
from . import views

app_name = 'studyApp'
urlpatterns = [
   path('study/<str:studyName>/',views.studies,name='study'),
   path('studyDetail/<int:id>/',views.studyDetail,name='studyDetail')
     
]