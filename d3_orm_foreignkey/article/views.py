from django.shortcuts import render
from .models import Article,Category,Tag
from frontuser.models import FrontUser,UserExtension
from django.http import HttpResponse

def index(request):
	articles = Article.objects.all()
	return render(request,'index.html',context = {"articles":articles})
	
def delete_view(request,categoryId):
	category = Category.objects.get(pk=categoryId)
	category.delete()
	return HttpResponse("A category is Deleted")

def insert_view(request):
	category = Category(name="Drawing")
	category.save()
	author= FrontUser(username="WMZha")
	author.save()
	article = Article(title='def',content='444')
	article.category = category
	article.author = author
	article.save()
	return HttpResponse("New Article is added")

def one_to_many_view(request):
	category = Category.objects.first()
	# If related_name is defined, category.article_set will be replaced by category.articles
	# article = category.article_set.first()
	article = category.articles.all()
	text = "category is %s" % article[0].title
	return HttpResponse(text)

def add_object_to_list(request):
	category = Category.objects.first()
	article = Article(title='g',content='7')
	article.author = FrontUser.objects.first()

	# article.save() # category_id is allowed to be null
	# category.articles.add(article)
	# category.save()

	# If category_id should be not null, we should avoid using save()
	category = Category.objects.first()
	category.articles.add(article,bulk=False)

	text = "article is %s" % category.articles.last().title
	return HttpResponse(text)

def one_to_one_view(request):
	frontUser = FrontUser.objects.first()
	# userExtension = UserExtension(address='HK')
	# userExtension.user = frontUser
	# userExtension.save()

	# userExtension = UserExtension.objects.first()
	# text = "userExtension is %s" % userExtension.user.username

	# text = "userExtension is %s" % frontUser.userextension.address
	text = "userExtension is %s" % frontUser.extension.address

	return HttpResponse(text)

def many_to_many_view(request):
	article = Article.objects.first()
	# tag = Tag(name='hot')
	# tag.save()
	# article.tag_set.add(tag)
	# text = "The last tag is %s" % article.tag_set.last().name

	tag = Tag.objects.get(pk=1)
	article = Article.objects.get(pk=5)
	tag.articles.add(article)
	tag.save()
	text = "The last article is %s" % tag.articles.last().content

	return HttpResponse(text)