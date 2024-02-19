from django.http  import HttpResponse

# Create your views here.
def book(request):
	return HttpResponse("Book Homepage")

def book_detail(request,book_id):
 	text = "book id is %s" % (book_id)
 	return HttpResponse(text)

def book_list(request):
	return HttpResponse("Book list page")