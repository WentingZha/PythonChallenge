from django.shortcuts import render
from django.http import HttpResponse

def iftag(request):

	# context = {
	# 	'age' : 18
	# }

	context = {
		'family' : [
			'WenTingZha',
			'LingZhiGu',
			'WeiMingZha',
			'WingHangHui'
		]
	}
	return render(request,'iftag.html',context =context)
	

def fortag(request):

	context = {
		'books' : [
			'Self Reference Engine',
			'Book of No Sleep',
			'Ender\'s Game'
		],

		'person' :{
			'username' : 'WenTingZha',
			'age' : '35',
			'height' : '174'
		},

		'family' :[
			{
			'name' : 'WenTingZha',
			'hobby' : 'Coding and Reading',
			'gender' : 'female'
			},
			{
			'name' : 'LZGu',
			'hobby' : 'Singing and Poker',
			'gender' : 'male'
			},
			{
			'name' : 'WMZha',
			'hobby' : 'Drawing and Cooking',
			'gender' : 'male'
			},
			{
			'name' : 'EternityHui',
			'hobby' : 'Calculation and Games',
			'gender' : 'male'
			},
		],

		'comments':[]
	}
	return render(request,'fortag.html',context =context)



def withtag(request):

	context = {
		'family' : [
			'WenTingZha',
			'LingZhiGu',
			'WeiMingZha',
			'WingHangHui'
		]
	}
	return render(request,'withtag.html',context =context)


def urlTag(request):

	context = {
		'family' : [
			'WenTingZha',
			'LingZhiGu',
			'WeiMingZha',
			'WingHangHui'
		]
	}
	return render(request,'urlTag.html',context =context)

def login(request):
	next = request.GET.get('next')
	text = 'Redirect to url: %s' % next 
	return HttpResponse(text)

def reading(request):
	return HttpResponse("Reading")

def book_detail(request,book_id):
	text = 'Book ID is %s' % book_id
	return HttpResponse(text)

def book_category(request,book_id,category_id):
	text = 'Book ID is %s, category is %s' % (book_id,category_id)
	return HttpResponse(text)

def news(request):
	return HttpResponse("News")

def boardGame(request):
	return HttpResponse("BoardGame")



def autoEscape(request):

	context = {
		'info': "<a href='www.google.com'>GOOGLE</a>"
	}
	return render(request,'autoEscape.html',context =context)
	

def verbatimTag(request):

	return render(request,'verbatimTag.html')
	
