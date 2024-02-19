
from django.http import HttpResponse

def book(request):
	return HttpResponse("Books page")