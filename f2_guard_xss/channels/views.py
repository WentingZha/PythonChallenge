from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Comment
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect,reverse
from django.template.defaultfilters import escape

def index(request):
	context = {
		'comments': Comment.objects.all()
	}
	return render(request,'index.html',context = context)

@csrf_exempt
@require_http_methods(['POST'])
def createComment(request):
	content = request.POST.get('content')
	# Change the website tags to characters before it is written into the DB
	content = escape(content)
	Comment.objects.create(content = content)
	return redirect(reverse('index'))
