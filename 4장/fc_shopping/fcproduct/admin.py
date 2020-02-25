from django.contrib import admin
from .models import Fcproduct
# Register your models here.

class FcproductAdmin(admin.ModelAdmin):
    list_display = ('name','price')

admin.site.register(Fcproduct,FcproductAdmin)