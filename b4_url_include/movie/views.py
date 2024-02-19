from django.http  import HttpResponse

# Create your views here.
def movie(request):
	return HttpResponse("Movie page")

def movie_list(request):
	return HttpResponse("Movie list page")