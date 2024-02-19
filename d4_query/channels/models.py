from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True,related_query_name='articles')
	createTime = models.DateTimeField(auto_now_add=True,null=True)
	def __str__(self):
		return "Article:(id:%s,title:%s,content:%s,category_id:%s,createTime:%s)" % (self.id,self.title,self.content,self.category_id,self.createTime)

class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return "Category:(id:%s,name:%s)" % (self.id,self.name)
