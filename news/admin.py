from django.contrib import admin
from .models import News, NewsCategory
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(NewsCategory, CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','slug','published_date', 'updated_date')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(News, NewsAdmin)