from catalog.models import Author, Book
from rest_framework import serializers

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'edition', 'publication_year', 'authors']
