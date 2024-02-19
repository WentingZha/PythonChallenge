from django.shortcuts import render

def index(request):
	context = {
		'username' : 'WentingZha'
	}
	return render(request,'index.html',context = context)

def company(request):
	context = {
		'username' : 'WentingZha'
	}
	return render(request,'company.html',context = context)
	
def school(request):
	context = {
		'username' : 'WentingZha'
	}
	return render(request,'school.html',context = context)
	