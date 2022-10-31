from random import choices
from secrets import choice
from unicodedata import name
from django.db import models

# Create your models here.

class Publisher(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    # numberOfBooksPublished = models.IntegerField()
    # numberOfAuthorsPublished = models.IntegerField()

class Author(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher,related_name="author" , null=True , on_delete = models.SET_NULL)

    
    def __str__(self):
        return self.name

class Book(models.Model):

    GENERE = (
        ("Fantasy","Fantasy"),
        ("Detective and Mystery","Detective and Mystery"),
        ("Horror","Horror"),
        ("Historic Fiction","Historic Fiction")

    )

    author = models.ForeignKey(Author,related_name = "book" , null=False , on_delete =models.CASCADE)
    publisher = models.ForeignKey(Publisher , related_name = "book", null=True , on_delete = models.SET_NULL)
    name = models.CharField(max_length=100)
    genere = models.CharField(max_length=100 , choices = GENERE)
    pages = models.IntegerField()
    price = models.IntegerField()



    def __str__(self):
        return self.name