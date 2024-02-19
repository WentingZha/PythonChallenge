from django.http  import HttpResponse
from django.shortcuts import reverse

def article(request):
	return HttpResponse("Article page")

def article_list(request, category):
	text ='Category is %s' % category
	return HttpResponse(text)

def article_detail(request, article_id):
	reverse('detail',kwargs={'article_id':article_id})
	return HttpResponse("Article Detail")
