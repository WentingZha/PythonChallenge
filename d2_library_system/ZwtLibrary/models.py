from django.db import models
from django.utils.timezone import now

# Pass a instance of models.Model 
# Create an ORM model mapping to DB
# Remember to add the app to the setting
class BestSeller(models.Model):
	bookId = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100,null=False)
	author = models.CharField(max_length=100,null=False)
	price = models.FloatField(null=False,default=0)

	def __str__(self):
		return "<Book:({name},{author},{price})>".format(name=self.name,author=self.author,price=self.price)

class Publisher(models.Model):
	name = models.CharField(max_length=100,null=False)
	address = models.CharField(max_length=100,null=True)

class Article(models.Model):
	articleId = models.BigAutoField(primary_key = True)
	removed = models.BooleanField()
	title = models.CharField(max_length=200,null=True)
	content = models.CharField(max_length=200,null=True)
	createTime = models.DateTimeField(auto_now_add = True)
	
class User(models.Model):
	email = models.EmailField()
	signature = models.TextField() #longtext type
	name = models.CharField(max_length=100,null=True)
	password = models.CharField(max_length=100,null=True)

class Writer(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(null=True,db_column='writerAge',default=0)
	createTime = models.DateTimeField(default=now )
	telephone = models.CharField(max_length=11,unique=True,null=True)

	def __str__(self):
		return "<Writer id: %s,createTime: %s)>" % (self.id,self.createTime)

	class Meta:
		# The default table name is [app name]_[class_name], you can change to [class name]
		db_table = 'writer'
		# The list will be queued by createTime, then id
		# If you add a minus before the field, the sequence will be reversed
		ordering = ['-createTime','id']
		


# Generate the migration files
# python manage.py makemigrations

# Mapping the new files to DB
# python manage.py migrate

# Insert a book
# book = BestSeller(name='Book of No Sleep',author='Reddit',price='98')
# book.save()

# book.delete()