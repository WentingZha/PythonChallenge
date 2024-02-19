
from django.http import HttpResponse

def movie(request):
	return HttpResponse("Movie page")