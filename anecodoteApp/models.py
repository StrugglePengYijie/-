from contextlib import nullcontext
from distutils.command.upload import upload
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
from django.utils import timezone

class anecodote(models.Model):
    PRODUCTS_CHOICES = (        
        ('附近趣事','附近趣事'),
        ('网络趣闻','网络趣闻'),
        
        )
    title = models.CharField(max_length=50,verbose_name='新闻中心')
    description =  description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='anecodote/images/',
                               filePath='anecodote/files/')
    anecodoteType = models.CharField(choices=PRODUCTS_CHOICES,max_length=50,verbose_name='分类大全')
    
    publishDate = models.DateTimeField(max_length=20,default=timezone.now,verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量',default=0)
    photo = models.ImageField(upload_to = 'anecodote/',blank = True,null = True,verbose_name='展报')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publishDate']
        verbose_name = "逸闻中心"
        verbose_name_plural = verbose_name
