from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('comment/', views.article_create, name="comment"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
