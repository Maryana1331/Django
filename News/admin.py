from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'created_at', 'photo', 'is_published')
    # длаем ссылками через админку поля id title
    list_display_links = ('id', 'title')
    # добавление поиска по полям
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'id')
    list_editable = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    # какие поля будут отображаться
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
