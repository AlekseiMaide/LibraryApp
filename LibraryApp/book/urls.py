from django.urls import path
from book import views

urlpatterns = [
    path('', views.book_list, name='get_books'),
    path('<int:pk>', views.lend_retrieve, name='lend_retrieve_book'),
]
