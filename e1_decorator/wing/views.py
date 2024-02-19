from django.shortcuts import render
from .models import Animal
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods,require_GET
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import reverse,redirect,reverse
from django.core.handlers.wsgi import WSGIRequest


@require_GET
def channels(request):
	username = request.GET.get('username')
	if username:
		return HttpResponse(username)
	else:
		return redirect(reverse('register'))
		
# @require_GET = @require_http_methods(['GET'])
@require_GET
def get_animals(request):
	animals = Animal.objects.all()
	return HttpResponse(animals)

# To solve 'CSRF verification failed.'
# 1. Delete the middleware from the list
# MIDDLEWARE = [
#     'django.middleware.csrf.CsrfViewMiddleware',
# ]
#
# 2. from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def someFunction(request):



# @csrf_exempt
# def add_animal(request):
# 	name = request.POST.get('name')
# 	age = request.POST.get('age')
# 	Animal.objects.create(name=name,age=age)
# 	return HttpResponse("Added")

@csrf_exempt
@require_http_methods(['POST','GET'])
def add_animal(request):
	if request.method == 'GET':
		return render(request,'add_animal.html')
	else:
		name = request.POST.get('name')
		age = request.POST.get('age')
		Animal.objects.create(name=name,age=age)
		return HttpResponse("Added")

def register(request):
	return HttpResponse("register")

# WSGIRequest
# http://127.0.0.1:8000/signin/?username=zha&age=35
def signin(request):
	# All the request information
	item = request.META.items()
	# Check the request is secure or not
	request.is_secure()
	
	return HttpResponse()

