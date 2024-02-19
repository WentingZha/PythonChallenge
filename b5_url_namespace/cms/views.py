from django.http  import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('CMS Page')

def login(request):
	return HttpResponse('CMS login')