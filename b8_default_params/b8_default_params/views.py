from django.http  import HttpResponse
from django.shortcuts import reverse,redirect

book_list = [
	'Self reference engine',
	'Book of No Sleep',
	'Ender\'s game'
]

def books(request,page = 0):
	return HttpResponse(book_list[page])