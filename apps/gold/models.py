from __future__ import unicode_literals

from django.db import models

# Create your models here.
  # Inside models.py

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name,self.desc)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    blog = models.ForeignKey(Blog, related_name="comments")

class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name="admins")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# this_author = Author.objects.get(id=2)
# my_book = Book.objects.create(title="Little Women", author=this_author)
# OR IN ONE LINE
# my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

#You can search based off a FK relationship
# this_author= Author.objects.get(id=2)
# books = Book.objects.filter(author=Author.objects.get(id=2))

# books = Book.objects.filter(author__name="Louise May Alcott")
# books = Book.onjects.filter(author__name__startwith = "Lou")

#this_book = Book.objects.get(id=4)
#this_publisher = Publisher.objects.get(id=2)
#this_publisher.books.add(this_book)

