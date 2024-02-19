from django.shortcuts import render
from django.db import connection

# http://127.0.0.1:8000/?animalId=2
# http://127.0.0.1:8000/?animalId=1 or 1=1
def home(request):
	animalId = request.GET.get('animalId')
	context = {}
	if animalId:
		cursor = connection.cursor()
		# sql = 'select id, username, age from animal where id=1 or 1=1'
		# cursor.execute(sql)
		cursor.execute("select id, name,age from animal where id=%s"%animalId)
		animalList = cursor.fetchall()
		context['animalList'] = animalList
	return render(request,'home.html',context=context)

# http://127.0.0.1:8000/getAnimalByName/?name=chicken
# http://127.0.0.1:8000/getAnimalByName/?name=chicken 'or' 1=1
def getAnimalByName(request):
	name = request.GET.get('name')
	context = {}
	if name:
		cursor = connection.cursor()
		sql = "select id, name, age from Animal where name='%s'" % name
		# sql = "select id, name from Animal where name='goose' or '1=1'" 
		cursor.execute(sql)
		animalList = cursor.fetchall()
		context['animalList'] = animalList
	return render(request,'getAnimalByName.html',context=context)

# How to protect your website from sql injection:
# 1. Always verify user's input.
# 2. Don't try to write sql string, use parameters to access the database.
# 3. Encode the important data.
# 4. Avoid using Administrator role.
# 5. Sql error message should not be sent to user.
# 6. In django, Use ORM instead of sql