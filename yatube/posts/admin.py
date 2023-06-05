from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "text", "pub_date", "author")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)
    # добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"
    # это свойство сработает для всех колонок: где пусто - там будет эта строка


class GroupAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "title", "description", "slug")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("title",)
    # добавляем возможность фильтрации по дате
    # list_filter = ("pub_date",)
# list_display — перечень свойств модели, которые мы хотим показать в интерфейсе. Если это свойство не указано — будет отображаться строка Имя_модели(идентификатор), как было с записью Post(1).
# search_fields — перечень полей, по которым будет искать поисковая система. Форма поиска отображается над списком элементов.
# list_filter — поля, по которым можно фильтровать записи. Фильтры отображаются справа от списка элемен
# class PostAdmin(admin.ModelAdmin):
#     # добавим в начало столбец pk
#     list_display = ("pk", "text", "pub_date", "author")
#     search_fields = ("text",)
#     list_filter = ("pub_date",)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)

