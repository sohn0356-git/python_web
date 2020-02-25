from django.contrib import admin
from .models import Tag
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)      #field들이 listing됨

admin.site.register(Tag,TagAdmin)