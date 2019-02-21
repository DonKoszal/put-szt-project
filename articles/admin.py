from django.contrib import admin
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Article, ArticleAdmin)