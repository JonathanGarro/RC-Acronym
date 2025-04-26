from django.contrib import admin
from .models import Acronym, Category

class AcronymAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'definition', 'category', 'created_by', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('acronym', 'definition')

admin.site.register(Acronym, AcronymAdmin)
admin.site.register(Category)
