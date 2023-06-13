from django.contrib import admin

from . models import Cartoon

# Register your models here.
class CartoonAdmin(admin.ModelAdmin):
    list_display = ['description','photo']

admin.site.register(Cartoon,CartoonAdmin)