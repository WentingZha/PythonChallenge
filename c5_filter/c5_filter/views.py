from django.shortcuts import render
from datetime import datetime

def index(request):
	context = {
		'greet':greet
	}
	return render(request,'index.html',context = context)

def greet():
	return "Hi, Eternity"

def add_view(request):
	context = {
		'value1':['1','2'],
		'value2':['3','4']

	}
	return render(request,'add.html',context)


def cut_view(request):
	return render(request,'cut.html')

def date_view(request):
	context = {
		'today': datetime.now()
	}
	return render(request,'date.html',context = context)

def default_view(request):
	context = {
		# 'value':'Hi Eternity'
		# 'value': {}
		'value': None
	}

	return render(request,'default.html',context = context)


def first_view(request):
	context = {
		'value': ['A','b','c ']
	}

	return render(request,'first.html',context = context)

def floatformat_view(request):
	context = {
		'value': 1.234
	}

	return render(request,'first.html',context = context)

def join_view(request):
	context = {
		'value': [1,2,3]
	}

	return render(request,'join.html',context = context)

def random_view(request):
	context = {
		'value': [1,2,3]
	}

	return render(request,'random.html',context = context)

def safe_view(request):
	context = {
		'value': "<script>alert('Hi, Eternity');</script>"
	}

	return render(request,'safe.html',context = context)

def slice_view(request):
	context = {
		'value': [1,2,3,4,5,6,7]
	}

	return render(request,'slice.html',context = context)

def striptags_view(request):
	context = {
		'value': '<script>alert("Hi, Eternity")</script>'
	}

	return render(request,'striptags.html',context = context)

def truncatechars_view(request):
	context = {
		# 'value': 'Eternity!'

		'value': '<p>Eternity!</p>'
	}

	return render(request,'truncatechars.html',context = context)