from django.http  import HttpResponse

# Create your views here.
def article(request):
	return HttpResponse("Article page")

def article_list(request, year):
	text ='The year you input is %s' % year
	return HttpResponse(text)

def article_list_month(request, month):
	text ='The month you input is %s' % month
	return HttpResponse(text)