from django.db import models

class Animal(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(null=True,default=0)

	class Meta:
		db_table = 'Animal'
	
	def __str__(self):
		return "Animal:(id:%s,name:%s,age:%s)" % (self.id,self.name,self.age)


