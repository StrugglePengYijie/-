from django.contrib import admin
from shareApp.models import article,coments
# Register your models here.  
class art(admin.ModelAdmin):
    list_display=['tit']
    # 创建类在admin管理界面显示数据时 显示自定义的字段这里 文章显示标题 评论显示name
class com(admin.ModelAdmin):
    list_display=['name']
admin.site.register(article,art)
admin.site.register(coments,com)

