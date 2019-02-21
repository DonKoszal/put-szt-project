from django.db import models
from django.contrib.auth.models import User

class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    thumb = models.ImageField(default='default.png', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    class Meta:
        verbose_name = "Blog Article"
        verbose_name_plural = "Blog Articles"
        ordering = ["-created"]