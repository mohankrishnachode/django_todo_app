from .views import BookList,book_details, add_books, delete_book, update_book, get_books
from django.urls import path

urlpatterns = [
    path('books/', BookList.as_view()),
    path('books/<int:pk>/', book_details, name='book-details'),
    path('books/add_book/', add_books, name='add_books'),
    path('books/get_books/',get_books, name='get_books'),
    path('books/update/<int:pk>', update_book, name='update_book'),
    path('books/delete_book/<int:pk>', delete_book, name='delete_book'),
]