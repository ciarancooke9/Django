from django.contrib import admin
from .models import Page, Show, Actor, Genre

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Page, PageAdmin)
admin.site.register(Show)
admin.site.register(Actor)
admin.site.register(Genre)
# Register your models here.
