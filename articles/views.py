from django.shortcuts import render, redirect
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
	articles = Article.objects.published()
	return render(request, 'articles/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        form = forms.AddComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article = article
            instance.author = request.user
            instance.save()
    form = forms.AddComment()
    comments = Comment.objects.filter(article=article)
    return render(request, 'articles/article_detail.html', { 'article': article, 'comments': comments, 'form': form } )
    
@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form })