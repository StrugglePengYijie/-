from django.contrib import admin
from .models import lineImg,line

# Register your models here.


class lineImgInline(admin.StackedInline):
    model = lineImg
    extra = 1     # 默认显示条目的数量

class lineAdmin(admin.ModelAdmin):
    inlines = [lineImgInline,]

admin.site.register(line, lineAdmin)
