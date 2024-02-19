from django.db import models
class FrontUser(models.Model):
	username = models.CharField(max_length=200,null=True)

class UserExtension(models.Model):
	address = models.CharField(max_length=100)
	user = models.OneToOneField("FrontUser",on_delete=models.CASCADE,related_name='extension')

	def __str__(self):
		return "<UserExtension:(id:%s,address:%s,userId:%s)>" % (self.id,self.address,self.user.id)