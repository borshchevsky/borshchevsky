from ckeditor.widgets import CKEditorWidget
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin

from .models import Category, Product, Tag, Profile, Subscriber, SMSLog


class FlatPageAdminNew(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminNew)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Subscriber)
admin.site.register(SMSLog)


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('title', 'date_created')
