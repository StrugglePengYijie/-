from django.urls import path
from . import views

app_name = 'lineApp'
urlpatterns = [
    path('lines/<str:lineName>/',views.lines,name='lines'),
    path('lineDetail/<int:id>/', views.lineDetail, name='lineDetail'),
]