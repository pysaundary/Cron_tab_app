from django.contrib import admin
from .models import Students
from django.utils.html import format_html
# Register your models here.
class StudentAdminModel(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html("<img src='{}' width='30' style='border-radius:50%;'>".format(object.profile_pic.url) )
        thumbnail.short_description="profile_pic"
    list_display=['thumbnail','name','sex']

admin.site.register(Students,StudentAdminModel)
