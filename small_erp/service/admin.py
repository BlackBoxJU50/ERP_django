from django.contrib import admin

# Register your models here.
from service.models import service



class ServiceAdmin(admin.ModelAdmin):
    list_display=['name','price']

admin.site.register(service,ServiceAdmin)