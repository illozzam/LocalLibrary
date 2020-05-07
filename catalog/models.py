from django.db import models

# Create your models here.

class Authors(models.Model):
    """Model representing authors"""
    author_name = models.CharField("Author's name", max_length=100)

    class Meta:
        abstract = True

class Book(Authors):
    """Model representing a book"""
    title = models.CharField("Book's name",max_length=200)
    edition = models.CharField("Edition",max_length=15)
    publication_year = models.DateField("Year of the publication")
    authors = models.ManyToManyField(Authors)


    def __str__(self):
        return self.title

