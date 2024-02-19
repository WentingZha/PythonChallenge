from django.shortcuts import render
from django.db import connection
from .models import BestSeller,Article,Writer
from django.http import HttpResponse
from django.utils.timezone import now,localtime

def get_cursor():
	return connection.cursor()

def index(request):
	cursor = get_cursor()
	cursor.execute("select id,name,author,price from book")
	books = cursor.fetchall()
	return render(request,'index.html',context = {"books":books})

def edit_book(request):
	bestSeller = BestSeller.objects.get(pk=2)
	bestSeller.price = 111
	bestSeller.save()

	# book.delete()
	return HttpResponse('Book is updated!')

def add_book(request):
	# bestSeller = BestSeller(name='Self Reference Engine',author='Toh Enjoe',price='100')
	# bestSeller.save()
	return HttpResponse('Best sellers are published!')

def book_detail(request):
	article = Article(removed = False,title = 'Channel',createTime = now())
	article.save()
	return render(request,'bookDetail.html',context = {"article":article})

def best_seller(request):
	# pk: primary key or use 'id'
	bestSeller = BestSeller.objects.get(pk=1)
	bestSeller = BestSeller.objects.filter(name='Self Reference Engine').first()
	return render(request,'bestSeller.html',context = {"bestSeller":bestSeller})

def user(request):
	# writer = Writer(name='Wing',age=31,telephone='3333333')
	# writer.save() 
	writers = Writer.objects.all()
	return render(request,'user.html',context = {"writers":writers})
	# return render(request,'user.html')

