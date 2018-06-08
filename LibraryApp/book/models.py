from django.db import models


class Book(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published = models.DateField()
    isbn = models.BigIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        db_table = 'book'
