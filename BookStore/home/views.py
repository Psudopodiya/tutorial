from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import *
from .serializers import *
from .models import *
# Create your views here.

def home(request):
    return HttpResponse("Hello there")

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookPost(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorPost(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherList(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherPost(CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer