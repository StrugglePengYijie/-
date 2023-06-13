from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField
# Create your models here.
class article(models.Model):
    tit = models.CharField('标题',max_length=200)
    img = models.FileField('图片',upload_to='media/img',)
    conten = UEditorField('内容')
    c_tim =models.DateTimeField(max_length=20,default=timezone.now,verbose_name='发布时间')
    def __str__(self):
        return self.tit
        
        # 为了后台数据显示清晰加此一条 这里显示文章标题方便查看
    class Meta:
        verbose_name = '文章内容'
        verbose_name_plural = '文章内容'
        ordering = ('-c_tim',)

class coments(models.Model):
    name = models.CharField('name',max_length=100)
    com = models.TextField('留言',blank=True, null=True)
    To = models.ForeignKey(to=article, on_delete=None, related_name='comen')
    tim = models.DateField(auto_now_add=True)

    # parent = models.ForeignKey('self',related_name='replies',verbose_name='父评论id',null=True,on_delete=None)
    def __str__(self):
        return self.name
        # 为了后台数据显示清晰加此一条 这里显示name方便查看
    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = '文章评论'
       