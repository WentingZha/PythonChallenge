from django.http  import HttpResponse
from django.shortcuts import redirect,reverse

# Create your views here.
def index(request):
	#Check the url if it is ended with username
	#http://127.0.0.1:8000/?username=1
	username = request.GET.get('username')
	if username:
		return HttpResponse('Frontend Page')
	else:
		# return redirect('/login/')
		# The mapping rule is defined in front/urls.py
		return redirect(reverse('front:login'))

def login(request):
	return HttpResponse('Frontend login')