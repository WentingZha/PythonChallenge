from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(['GET','POST'])
def transfer(request):
	if request.method == 'GET':
		return render(request,'transfer.html')
	else:
		email = request.POST.get('email')
		total = request.POST.get('total')
		return HttpResponse('Done!')

# def transfer(request):
    # return render(request, 'transfer.html')

def channels(request):
	return HttpResponse("channels")
