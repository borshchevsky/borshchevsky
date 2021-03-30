from ckeditor.widgets import CKEditorWidget
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin

from .models import Category, Product, Tag


class FlatPageAdminNew(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminNew)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    ordering = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...

