from django.shortcuts import render
from django.http.request import QueryDict
from django.http import HttpResponse,JsonResponse,StreamingHttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
import csv
from django.template import loader

def channels(request):
	username = request.GET.get('username',default='1')
	return HttpResponse(username)

@csrf_exempt
@require_http_methods(['GET','POST'])
def addChannel(request):
	if request.method == 'GET':
		return render(request,'add_channel.html')
	else:
		title = request.POST.get('title')
		content = request.POST.get('content')
		tags = request.POST.getlist('tags')
		return HttpResponse(str(title)+str(content)+str(tags))

def httpResponse(request):
	response = HttpResponse()
	response.content = 'LZ Class'

	response = HttpResponse('<h1>LZ Class</h1>')

	response = HttpResponse('<h1>LZ Class</h1>',content_type='text/plain;charset=utf-8')

	response['password'] = 'LZ Lesson'

	response['Z-Token'] = 'Z-Token'
	
	# response.status_code = 400

	response.write('LZ Class')

	return response

def jsonResponse(request):
	person = {
		'username':'LZ',
		'age':2,
		'height':122
	}

	# person_str = json.dumps(person)
	# response = HttpResponse(person_str,content_type='application/json')

	response = JsonResponse(person) 


	people = [
		{
			'username':'LZ',
			'age':2,
			'height':122

		},
		{
			'username':'WentingZha',
			'age':111,
			'height':173

		}
	]

	response = JsonResponse(people,safe=False) 
	return response

def csvView(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = "attachment;filename=Hang.csv"
	writer = csv.writer(response)
	writer.writerow(['username','hobby'])
	writer.writerow(['Hang','game'])
	return response


def csvTemplate(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = "attachment;filename=Hang.csv"
	context = {
		'rows':[
			['username','hobby'],
			['Hang','game']
		]

	}
	template = loader.get_template('Hang.txt')
	csv_template=template.render(context)
	response.content = csv_template
	return response

def largeCsvFile(request):
	response = StreamingHttpResponse(content_type='text/csv')
	response['Content-Disposition'] = "attachment;filename=Hang.csv"
	row = ("Row {}, {}\n".format(row,row) for row in range(0,100000))
	# response.streaming_content = ("username,age\n","Hang,35\n")
	response.streaming_content = row
	return response