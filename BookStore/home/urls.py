from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path("",home,name="home"),
    path("books/list",BookList.as_view(),name="bookList"),
    path("books/post",BookPost.as_view(),name="bookList"),
    path("authors/list",AuthorList.as_view(),name="authorList"),
    path("authors/post",AuthorPost.as_view(),name="authorPost"),
    path("publishers/list",PublisherList.as_view(),name="publisherList"), 
    path("publishers/post",PublisherPost.as_view(),name="publisherList") 
]