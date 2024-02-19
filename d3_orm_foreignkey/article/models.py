from django.db import models
from django.utils.timezone import now

class Category(models.Model):
	name = models.CharField(max_length=100,null=True)
	def __str__(self):
		return "<Category:(id:%s,name:%s)>" % (self.id,self.name)


class Article(models.Model):
	title = models.CharField(max_length=200,null=True)
	content = models.CharField(max_length=200,null=True)
	# Related with another table
	# ForeignKey(model_name, method 'on_delete')
	# on_delete=models.CASCADE means the related data will be deleted
	# If related_name is defined, category.article_set will be replaced by category.articles
	category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True,related_name='articles')
	# Link with another app
	author = models.ForeignKey("frontuser.FrontUser",on_delete=models.CASCADE,null=True)

	# Important data should not be deleted
	# category = models.ForeignKey("Category",on_delete=models.PROTECT)

	# If Article data is deleted, category will be null
	# category = models.ForeignKey("Category",on_delete=models.SET_NULL)

	# If Article data is deleted, category will be set to the default value
	# category = models.ForeignKey("Category",on_delete=models.SET_DEFAULT)

	# If Article data is deleted, category will be set to another value
	# category = models.ForeignKey("Category",on_delete=models.SET(Category.objects.get(pk=1)))

	def __str__(self):
		return "<Article:(id:%s,title:%s)>" % (self.id,self.title)

class Comment(models.Model):
	content = models.TextField()
	# Refer to self
	originComment = models.ForeignKey("self",on_delete=models.CASCADE,null=True)

class Tag(models.Model):
	name = models.CharField(max_length=100)
	articles = models.ManyToManyField("Article",related_name='tags')
