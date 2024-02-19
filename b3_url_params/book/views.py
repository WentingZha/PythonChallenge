from django.shortcuts import render
from django.http  import HttpResponse
from django.urls import converters

# Create your views here.
def book(request):
	return HttpResponse("Book Homepage")

#http://127.0.0.1:8000/book/detail/1
# def book_detail(request,book_id):
#  	text = "book id is %s" % book_id
#  	return HttpgoryResponse(text)	

#http://127.0.0.1:8000/book/detail/1/2
def book_detail(request,book_id,category_id):
 	text = "book id is %s, category is %s" % (book_id, category_id)
 	return HttpResponse(text)	

#http://127.0.0.1:8000/book/author/?id=1
def author_detail(request):
 	# author_id = request.GET.get('id')
 	author_id = request.GET['id']
 	text = 'Id of author is %s' % author_id
 	return HttpResponse(text)

def publisher_detail(request,publisher_id):
 	text = 'Id of publisher is %s' % publisher_id
 	return HttpResponse(text)