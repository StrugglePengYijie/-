from contextlib import nullcontext
from tabnanny import verbose
from turtle import title
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
from django.utils import timezone

class study(models.Model):
    PRODUCTS_CHOICES = (        
        ('python','python'),
        ('linux','linux'),
       # ('小说摘抄','小说摘抄'),
        )
    title = models.CharField(max_length=50,verbose_name='标题')
    description = models.TextField(verbose_name='简介')
    
    description2 = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='study/images/',
                               filePath='study/files/')
    studyType = models.CharField(choices=PRODUCTS_CHOICES,max_length=50,verbose_name='分类大全')
    publishDate = models.DateTimeField(max_length=20,default=timezone.now,verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量',default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '学习中心'
        verbose_name_plural = '学习中心'
        ordering = ('-publishDate',)


