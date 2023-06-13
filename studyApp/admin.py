from django.contrib import admin
from .models import study
# Register your models here.

class studyAdmin(admin.ModelAdmin):
    style_fields = {'description2': 'ueditor'}

admin.site.register(study,studyAdmin)
