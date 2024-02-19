from django.shortcuts import render
from .models import Article,Category
from django.http import HttpResponse
from datetime import datetime,time
from django.utils.timezone import make_aware

def index(request):

	category = Category.objects.all()

	article = Article.objects.all()

	# filter() function return QuerySet
	# get() function return Artical Model
	article = Article.objects.filter(id__exact=1)

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content" 
	# FROM "channels_article" WHERE "channels_article"."id" = 1
	query = article.query

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content" 
	# FROM "channels_article" WHERE "channels_article"."title" LIKE second Book '\'
	# 'exact' is similiar to '=', iexact is similiar to 'like'
	article = Article.objects.filter(title__iexact="Book")

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content" 
	# FROM "channels_article" WHERE "channels_article"."title" LIKE %Sleep% ESCAPE '\'
	article = Article.objects.filter(title__contains='Sleep')

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content" 
	# FROM "channels_article" WHERE "channels_article"."id" IN (1, 2, 3)	
	article = Article.objects.filter(id__in=[1,2,3])

	# Check the category name of articles id is 1, 2 or 3
	categories = Category.objects.filter(articles__id__in=[1,2,3])

	# Check the category of all the articles which contain "Game" in the title
	# SELECT "channels_category"."id", "channels_category"."name" 
	# FROM "channels_category" INNER JOIN "channels_article" 
	# ON ("channels_category"."id" = "channels_article"."category_id") 
	# WHERE "channels_article"."id" IN 
	# (SELECT U0."id" FROM "channels_article" U0 WHERE U0."title" LIKE %Game% ESCAPE '\')
	articles = Article.objects.filter(title__contains='Game')
	categories = Category.objects.filter(articles__in=articles)

	return HttpResponse(categories)

def insert_article(request):
	article = Article(title='Self Reference Engine',content='A battle between Old Wisdom and New Generation.')
	article.save()
	article = Article(title='Book of No Sleep',content='On a second thought, it is horrible.')
	article.save()
	article = Article(title='Shao Nao X',content='A strange world')
	article.save()
	article = Article(title='Ender\'s Game',content='A war controlled by a gamer.')
	article.save()

	category = Category(name='Science Observer')
	category.save()
	category = Category(name='Hot')
	category.save()
	return HttpResponse("added")

def edit_article(request):
	articles = Article.objects.all()
	for article in articles:
		article.category = Category.objects.first()

	article = Article.objects.first()
	article.category = Category.objects.last()
	article.save()

	article = Article.objects.last()
	article.category = Category.objects.last()
	article.save()

	return HttpResponse("updated")

def check(request):
	# Check all the articles that id is greater than 2
	articles = Article.objects.filter(id__gt=2)

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id"
	# FROM "channels_article" WHERE "channels_article"."id" >= 2
	articles = Article.objects.filter(id__gte=2)

	# Check all the articles that id is lower than 2
	articles = Article.objects.filter(id__lt=2)

	articles = Article.objects.filter(id__lte=2)
	return HttpResponse(articles)

def check2(request):
	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id" 
	# FROM "channels_article" WHERE "channels_article"."title" LIKE Self% ESCAPE '\'
	# articles = Article.objects.filter(title__startswith="self")

	# articles = Article.objects.filter(title__endswith="Game")

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id", "channels_article"."createTime" 
	# FROM "channels_article" WHERE "channels_article"."createTime" BETWEEN 2024-02-05 02:00:00 AND 2024-02-05 03:00:00
	startTime = make_aware(datetime(year=2024,month=2,day=5,hour=2,minute=0,second=0))
	endTime = make_aware(datetime(year=2024,month=2,day=5,hour=3,minute=0,second=0))
	articles = Article.objects.filter(createTime__range=(startTime,endTime))
	return HttpResponse(articles)

def check3(request):
	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id", "channels_article"."createTime" 
	# FROM "channels_article" WHERE django_datetime_cast_date("channels_article"."createTime", UTC, UTC) = 2024-02-05
	# articles = Article.objects.filter(createTime__date=datetime(year=2024,month=2,day=5))

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id", "channels_article"."createTime" 
	# FROM "channels_article" WHERE "channels_article"."createTime" BETWEEN 2024-01-01 00:00:00 AND 2024-12-31 23:59:59.999999
	articles = Article.objects.filter(createTime__year=2024)

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id", "channels_article"."createTime" 
	# FROM "channels_article" WHERE "channels_article"."createTime" >= 2024-01-01 00:00:00
	articles = Article.objects.filter(createTime__year__gte=2024)

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id", "channels_article"."createTime" 
	# FROM "channels_article" WHERE django_datetime_extract(week_day, "channels_article"."createTime", UTC, UTC) = 2
	# Sunday is the first day in UTC
	articles = Article.objects.filter(createTime__week_day=2)

	startTime = time(hour=2,minute=22,second=8)
	endTime = time(hour=2,minute=22,second=9)
	# articles = Article.objects.filter(createTime__time=time(hour=2,minute=22,second=8))
	articles = Article.objects.filter(createTime__time__range=(startTime,endTime))

	return HttpResponse(articles)


def check4(request):
	# article= Article.objects.first()
	# article.createTime = None
	# article.save()

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id", "channels_article"."createTime" 
	# FROM "channels_article" WHERE "channels_article"."createTime" IS NOT NULL
	articles = Article.objects.filter(createTime__isnull=False)

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id", "channels_article"."createTime" 
	# FROM "channels_article" WHERE "channels_article"."title" REGEXP ^Self
	articles = Article.objects.filter(title__regex=r"^Self")

	# SELECT "channels_article"."id", "channels_article"."title", "channels_article"."content", "channels_article"."category_id", "channels_article"."createTime" 
	# FROM "channels_article" WHERE "channels_article"."title" REGEXP '(?i)' || ^self
	articles = Article.objects.filter(title__iregex=r"^self")
	return HttpResponse(articles.query)