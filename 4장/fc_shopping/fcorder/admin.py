from django.contrib import admin
from .models import Fcorder
# Register your models here.

class FcorderAdmin(admin.ModelAdmin):
    list_display = ('fcuser','fcproduct')

admin.site.register(Fcorder,FcorderAdmin)