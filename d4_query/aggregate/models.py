from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'author'

    def __str__(self):
        return "Author:(id:%s,name:%s,age:%s,email:%s)" % (self.id,self.name,self.age,self.email)


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'publisher'

    def __str__(self):
        return "Publisher:(id:%s,name:%s)" % (self.id,self.name)

def pubilsher_default():
    return Publisher.objects.get_or_create(name="Default")

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.FloatField()
    rating = models.FloatField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_DEFAULT,default=pubilsher_default)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return "Book:(id:%s,name:%s,pages:%s,price:%s,rating:%s,author:%s,publisher:%s)" % (self.id,self.name,self.pages,self.price,self.rating,self.author_id,self.publisher_id)

class BookOrder(models.Model):
    book = models.ForeignKey("Book",on_delete=models.CASCADE)
    price = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'book_order'
        ordering = ['-create_time','price']

    def __str__(self):
        return "BookOrder:(id:%s,book:%s,price:%s,create_time:%s)" % (self.id,self.book_id,self.price,self.create_time)
