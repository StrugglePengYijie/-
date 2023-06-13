from django.contrib import admin
from .models import anecodote
# Register your models here.

class AnecodoteAdmin(admin.ModelAdmin):
    style_fields = {'description': 'ueditor'}

admin.site.register(anecodote,AnecodoteAdmin)
