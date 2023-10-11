from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg, Max, Min


def index(request):
    books = Book.objects.all()
    total_number_of_books = books.count()
    average_rating = books.aggregate(Avg('rating'))

    return render(request, 'index.html', {
        'books': books,
        'total_number_of_books': total_number_of_books,
        'average_rating': average_rating,
    })


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestselling': book.is_bestselling
    })
