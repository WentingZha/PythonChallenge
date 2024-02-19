from django.shortcuts import render
from django.http import HttpResponse
from news.models import Article,Tag
from .models import User

def index(request):
	# article = Article(title='abc',content='111')
	# author = User.objects.create(username='wentingzha',password='111')
	# article.author = author
	# article.save()
	return HttpResponse(Article.objects.last().content)
