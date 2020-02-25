
from django.contrib import admin
from .models import Fcuser
# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username','password','useremail')      #field들이 listing됨

admin.site.register(Fcuser,FcuserAdmin)