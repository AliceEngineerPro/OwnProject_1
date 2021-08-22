from django.contrib import admin

# Register your models here.
from app01 import models


@admin.register(models.Book,)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'publish')  # 显示默认字段
    # list_editable = ('name', 'price', 'author')
    # filter_horizontal = ('publish', 'id')  # 水平
    # filter_vertical = ()  # 垂直
    list_per_page = 2  # 分页
    search_fields = ('id', 'name', 'publish__name', 'price')  # 搜索
    list_filter = ('publish', 'date')  # 过滤器


@admin.register(models.Publish)
class PublishAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BookAndAuthor)
class BookAndAuthorAdmin(admin.ModelAdmin):
    pass

