from django.shortcuts import render
from .models import Author,Publisher,Book,BookOrder
from django.http import HttpResponse
from django.db.models import Avg,Count,Max,Min,Sum,F,Q,Prefetch
from django.db import connection

def insertAggr(request):
	author = Author(name='Toh Enjoe',age=35,email='Toh@gmail.com')
	author.save()
	author = Author(name='King',age=62,email='king@gmail.com')
	author.save()
	author = Author(name='Reddit',age=35,email='Reddit@yahoo.com')
	author.save()
	author = Author(name='Orson',age=57,email='Orson@gmail.com')
	author.save()


	publisher = Publisher(name='A')
	publisher.save()

	publisher = Publisher(name='B')
	publisher.save()
	
	book = Book(name='Self Reference Engine',pages=100,price=100,rating=5)
	book.author = (Author.objects.all())[0]
	book.publisher = (Publisher.objects.all())[0]
	book.save()

	book = Book(name='Book of No Sleep',pages=98,price=98,rating=4.8)
	book.author = (Author.objects.all())[1]
	book.publisher = (Publisher.objects.all())[1]
	book.save()

	book = Book(name='Ender\'s Game',pages=130,price=130,rating=4.6)
	book.author = (Author.objects.all())[2]
	book.publisher = (Publisher.objects.all())[1]
	book.save()

	book = Book.objects.filter(name__contains='Self Reference Engine').first()
	order = BookOrder(book=book,price = 100 )
	order.save()
	book = Book.objects.filter(name__contains='Book of No Sleep').first()
	order = BookOrder(book=book,price = 111 )
	order.save()
	book = Book.objects.filter(name__contains='Ender\'s Game').first()
	order = BookOrder(book=book,price = 100 )
	order.save()
	book = Book.objects.filter(name__contains='Self Reference Engine').first()
	order = BookOrder(book=book,price = 100 )
	order.save()
	book = Book.objects.filter(name__contains='Self Reference Engine').first()
	order = BookOrder(book=book,price = 120 )
	order.save()
	return HttpResponse("inserted")

def checkAggr(request):
	authors = Author.objects.all()
	publishers = Publisher.objects.all()
	books = Book.objects.all()
	orders = BookOrder.objects.all()
	return HttpResponse(orders)

def checkAvg(request):
	result = Book.objects.aggregate(price_avg=Avg("price"))
	#print the sql of a 'diction'
	queries = connection.queries

	return HttpResponse(result.get("price_avg"))
 
	
def checkAnnotion(request):

	# {'sql': 'SELECT AVG("book"."price") AS "price__avg" FROM "book"', 'time': '0.000'}{'sql': 'SELECT AVG("book_order"."price") AS "order_price_avg" 
	# FROM "book" LEFT OUTER JOIN "book_order" ON ("book"."id" = "book_order"."book_id")', 'time': '0.000'}
	result = Book.objects.aggregate(avg=Avg("bookorder__price"))

	#Get the avgerage price of every book
	# SELECT "book"."id", "book"."name", "book"."pages", "book"."price", "book"."rating", "book"."author_id", "book"."publisher_id", AVG("book_order"."price") AS "avg" 
	# FROM "book" LEFT OUTER JOIN "book_order" 
	# ON ("book"."id" = "book_order"."book_id") 
	# GROUP BY "book"."id", "book"."name", "book"."pages", "book"."price", "book"."rating", "book"."author_id", "book"."publisher_id"
	books = Book.objects.annotate(avg=Avg("bookorder__price"))

	# Add a new field to each insatnce of the QuerySet
	books = Book.objects.annotate(author_name=F('author__name'))
	return HttpResponse(books[0].author_name)

def checkCount(request):
	# Count the number of the books in 'book' table
	result = Book.objects.aggregate(book_nums=Count("id"))

	# Count the number of different emails
	# author = Author(name='zwt',age=35,email='wentingzha@gmail.com')
	# author.save()
	result = Author.objects.aggregate(email_nums=Count('email',distinct=True))

	# Count the number of every book in 'bookorder' table
	# Count("bookorder__id") is the same with Count("bookorder")
	books = Book.objects.annotate(book_nums=Count("bookorder"))

	# return HttpResponse(result.get('email_nums'))
	return HttpResponse(books[1].book_nums)

def checkMaxMin(request):
	result = Author.objects.aggregate(max=Max('age'),min=Min('age'))

	# Check the highest price and the lowest price of every book in the orders
	books = Book.objects.annotate(max=Max('bookorder__price'),min=Min('bookorder__price'))

	return HttpResponse(books[0].min)

 
def checkSum(request):
	# Gross sales of all the books
	result = BookOrder.objects.aggregate(total=Sum('price'))

	# Gross sales of each book
	books = Book.objects.annotate(total=Sum('bookorder__price'))

	# Gross sales of all the books in 2024
	result = BookOrder.objects.filter(create_time__year=2024).aggregate(total=Sum('price'))

	# Gross sales of each book in 2024
	books = Book.objects.filter(bookorder__create_time__year=2024).annotate(total=Sum('bookorder__price'))
	return HttpResponse(books[0].total)
 

def Ffunction(request):
	# employees = Employee.objects.all()
	# for employee in emplyees:
	#	  employee.salary += 1000
	# 	  emplayee.save()
    # Book.objects.update(price=F("price")+10)
    # books = Book.objects.all()

 	# authors = Author.objecs.all()
	# for author in authors:
	# 	  if author.name = author.email
	# 			print(author)
	author = Author(name='WentingZha',age=35,email='WentingZha')
	author.save()
	authors = Author.objects.filter(name=F("email"))
	return HttpResponse(authors)

def QFunction(request):
	# Q is for complicated sql query
	# Check all the books which price is lower than 10 or rating is higher than 4
	books = Book.objects.filter(Q(price__lte=10) | Q(rating__gte=4))

    # Check all the books whose price is higher than 100. And make sure they don't contains character 'De'
	books = Book.objects.filter(Q(price__gte=100)&~Q(name__contains='De'))

	books = Book.objects.filter(id__gte=2).filter(~Q(id=3))

	return HttpResponse(books)


def excludeFunction(request):
	# books = Book.objects.filter(id__gte=2).filter(~Q(id=3))
	books = Book.objects.filter(id__gte=2).exclude(id=3)
	return HttpResponse(books)

def orderby(request):
	books = BookOrder.objects.order_by("-create_time")

	# Check the books in desending order by create_time.
	# if create_time is the same, queue in desending order by price
	books = BookOrder.objects.order_by("-create_time","-price")

	books = BookOrder.objects.order_by("book__rating")

	# If several order_bys appear in the query sentence, only the last one will affect the result
	books = BookOrder.objects.order_by("create_time").order_by("book__rating")

	# We can define a default ordering value in 'Meta'
	# ordering = ['-create_time,price']

	books = BookOrder.objects.annotate(order_nums=Count('id')).order_by('-order_nums')
	return HttpResponse(books)

# Use 'values' function to extract some of the fields instead of all the fields
def values(request):
	# Return dictionary
	books = Book.objects.values("id","name","author__name")

	books = Book.objects.values("id","name",order_nums=Count("bookorder"))

	# Return string list
	books = Book.objects.values_list()

	books = Book.objects.values_list('id','name')

	books = Book.objects.values_list('id','name',flat = True)
	return HttpResponse(books)

def selectRelated(request):
	books = Book.objects.select_related('author')
	return HttpResponse(books[0].author.name)

# Many to many Search or one to one search, reduce the query times
def prefetchRelated(request):
	# books = Book.objects.all()
	# for book in books:
	# 	print('='*30)
	# 	print(book.name)
	# 	orders = book.bookorder_set.all()
	# 	for order in orders:
	# 		print(order.id)

	books = Book.objects.prefetch_related('bookorder_set')
	print(books[1].price)
	for book in books:
		orders = book.bookorder_set.filter(price__gte=30)

	# prefetch = Prefetch('bookorder_set',queryset=BookOrder.objects.filter(price__lte=50))
	# books = Book.objects.prefetch_related(prefetch)
	return HttpResponse(books[1].price)

def getFunction(request):
	# get() returns only one object
	book = Book.objects.get(id=1)

	# count() is more efficient than len()
	bookListLen = len(Book.objects.all())
	count = Book.objects.count()

	result = Book.objects.filter(name='IT').exists()

	# Use distinct() to remove duplicated data
	books = Book.objects.filter(bookorder__price__gte=100).distinct()

	books = Book.objects.annotate(order__price=F('bookorder__price')).filter(bookorder__price__gte=100).order_by('bookorder__price').distinct()


	return HttpResponse(books)

def createFunction(request):
	# publisher = Publisher(name="The Commercial Press")
	# publisher.save()

	# publisher = Publisher.objects.create(name="Joint Publishing")

	publisher = Publisher.objects.get_or_create(name="Asmodee")

	# publisher = Publisher.objects.bulk_create([
	# 	Publisher(name='123 Press'),
	# 	Publisher(name='ABC Press')
	# ])
	return HttpResponse(Publisher.objects.all())

def updateFunction(request):

	# Book.objects.update(price=F('price')+5)

	Author.objects.filter(id__gte=5).delete()

	return HttpResponse(Author.objects.all())

def slice(request):

	# books = Book.objects.all()[1:3]
	books = Book.objects.all()[0:2:2]
	return HttpResponse(books)