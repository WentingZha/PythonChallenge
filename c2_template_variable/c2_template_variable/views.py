from django.shortcuts import render
from django.http import HttpResponse

class Person(object):
	def __init__(self,username):
		self.username = username

def index(request):

	# Pass a string
	# context = {
	# 	'username':'WentingZha'
	# }

	# Pass an object
	# p = Person("WentingZha")
	# context = {
	# 	'person' : p
	# }

	# Pass a dictionary
	# p = Person("WentingZha")
	# context = {
	# 	'person' : {
	# 		'username' : 'WentingZha',
	# 		'keys'	: 'abc'
	# 	}
	# }

	# Pass a list
	p = Person("WentingZha")
	context = {
		'family' : [
			'WenTingZha',
			'LingZhiGu',
			'WeiMingZha',
			'WingHangHui'
		]
		
	}

	return render(request,'index.html',context =context)

