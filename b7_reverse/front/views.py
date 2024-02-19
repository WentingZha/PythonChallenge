from django.http  import HttpResponse
from django.shortcuts import reverse,redirect

def index(request):
	username = request.GET.get('username')
	if username:
		return HttpResponse("First page")
	else:
		# login_url = reverse('login')
		# return redirect(login_url)

		# In reverse function , kwargs is keyword arguments
		# This is an auto-login example
		detail_url = reverse('detail', kwargs = {"article_id":1})
		return redirect(detail_url)


def login(request):

	return HttpResponse("Login")

def article_detail(request, article_id):
	text = 'Id of your article is %s' % article_id
	return HttpResponse(text)