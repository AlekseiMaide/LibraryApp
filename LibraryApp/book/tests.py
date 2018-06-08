import json

from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from book.models import Book
from book.serializers import BookSerializer


# initialize the APIClient app
client = Client()


class GetAllBooksTest(TestCase):
    """ Test retrieving all books."""

    def setUp(self):
        Book.objects.create(
            title='Eloquent JavaScript, Second Edition',
            description='JavaScript lies at the heart of almost every modern web application',
            author='Marijn Haverbeke',
            published='2012-07-01',
            isbn=9781593275846)

        Book.objects.create(
            title='Learning JavaScript Design Patterns',
            description='With Learning JavaScript Design Patterns, you will learn how to write beautiful...',
            author='Addy Osmani',
            published='2012-07-01',
            isbn=9781449331818)

        Book.objects.create(
            title='Speaking JavaScript',
            description='Like it or not, JavaScript is everywhere these days-from browser to server...',
            author='Axel Rauschmayer',
            published='2014-02-01',
            isbn=9781449365035)

    def test_get_all_books(self):
        response = client.get(reverse('get_books'))

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LendBookTest(TestCase):
    """ Test Lending a book via PUT request."""

    def setUp(self):
        Book.objects.create(
            id=2,
            title='Speaking JavaScript',
            description='Like it or not, JavaScript is everywhere these days-from browser to server...',
            author='Axel Rauschmayer',
            published='2014-02-01',
            isbn=9781449365035,
            available=False)

        self.valid_args = {
            'available': False
        }
        self.invalid_args = {
            'available': 12323
        }

    def test_valid_lend_retrieve_book_request(self):
        response = client.put(
            reverse('lend_retrieve_book', kwargs={'pk': 2}),
            data=json.dumps(self.valid_args),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_lend_retrieve_book_request(self):
        response = client.put(
            reverse('lend_retrieve_book', kwargs={'pk': 2}),
            data=json.dumps(self.invalid_args),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
