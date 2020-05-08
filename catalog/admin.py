from django.contrib import admin
from .models import Author, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_year']

admin.site.register(Author)
