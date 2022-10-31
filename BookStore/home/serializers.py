from rest_framework import serializers
from .models import *

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer(read_only=True)
    class Meta:
        model =Author
        fields = ("name","publisher")


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer(read_only=True)
    author = AuthorSerializer(read_only =True)
    class Meta:
        model = Book
        fields = ("name","author","publisher","genere","pages","price")