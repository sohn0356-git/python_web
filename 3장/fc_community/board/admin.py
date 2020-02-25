
from django.contrib import admin
from .models import Board
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title','registered_dttm')      #field들이 listing됨

admin.site.register(Board,BoardAdmin)