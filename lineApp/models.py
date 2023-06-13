from contextlib import nullcontext
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
from django.utils import timezone

class line(models.Model):
    PRODUCTS_CHOICES = (        
        ('动漫语录','动漫语录'),
        ('书籍名句','书籍名句'),
        ('小说摘抄','小说摘抄'),
        )
    title = models.CharField(max_length=50,verbose_name='出自')
    description = models.TextField(verbose_name='详情描述')
    lineType = models.CharField(choices=PRODUCTS_CHOICES,max_length=50,verbose_name='分类大全')
    description2 = models.TextField(verbose_name='经典语录')
    description3 = models.TextField(verbose_name='个人评价')
    publishDate = models.DateTimeField(max_length=20,default=timezone.now,verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量',default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '经典语录'
        verbose_name_plural = '经典语录'
        ordering = ('-publishDate',)


class lineImg(models.Model):
    line = models.ForeignKey(line,related_name='lineImgs',verbose_name='经典语录',on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'line/',blank=True,verbose_name='图片')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'
    
