from django.shortcuts import render
from django.db import connection

def index(request):
	cursor = connection.cursor()
	# cursor.execute("insert into book(id,name,author) values(null,'Self Reference Engine','Toh Enjoe')")
	cursor.execute("select id,name,author from book")
	rows = cursor.fetchall()
	context = {
		'row' : rows
	}
	return render(request,'index.html',context = context)