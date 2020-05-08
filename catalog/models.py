from django.db import models

# Create your models here.

class Author(models.Model):
    """Model representing authors"""
    name = models.CharField("Author's name", max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model representing a book"""
    title = models.CharField("Book's name",max_length=200)
    edition = models.CharField("Edition",max_length=15)
    publication_year = models.DateField("Year of the publication")
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
