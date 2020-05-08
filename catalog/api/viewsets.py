from catalog.models import Author, Book
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows authors to be viewed and edited.
    '''
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows books to be viewed and edited.
    '''
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
