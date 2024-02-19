from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

#Add path to settings:
# import os
# SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
# TEMPLATES = [
#    {
#        'DIRS': [os.path.join(SETTINGS_PATH,'templates')],
#    },
#]
def index(request):
	#html = render_to_string("index.html")
	#return HttpResponse(html)

	return render(request,"index.html")

def slice_view(request):
	context = {
		"value":[1,2,3,4]
	}
	return render(request,'slice.html',context =context)

def striptags_view(request):
	context = {
		'value':'<script>alert("Chat")</script>'
	}
	return render(request,'striptags.html',context =context)

def truncatechars_view(request):
	context = {

		# 'value':'Shanghai...'

		# display the html tag
		'value':'<p>Shanghai...<p>'
	}
	return render(request,'truncatechars.html',context =context)
