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
    author = AuthorSerializer(read_only =True)
    class Meta:
        model = Book
        fields = ("name","genere","author","pages","price")