from django.contrib import admin
from .models import Page, Show, Actor, Genre

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title',)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('title','display_genre', 'display_actor', 'release')

admin.site.register(Page, PageAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Actor)
admin.site.register(Genre)
# Register your models here.
