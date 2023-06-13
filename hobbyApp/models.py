from distutils.command.upload import upload
from pydoc import describe
from tabnanny import verbose
from django.db import models

# Create your models here.
class Cartoon(models.Model):
    description = models.TextField(max_length=500,blank=True,null=True,verbose_name='动漫简介',)
    photo = models.ImageField(upload_to = 'cartoon',blank=True,verbose_name='图片',)

    class Meta:
        
        verbose_name = "动漫"
        verbose_name_plural = "动漫"