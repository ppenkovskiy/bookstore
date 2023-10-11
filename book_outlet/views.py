from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html',
                  {'books': books}
                  )


def book_detail(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    # the same below in 1 line of code
    book = get_object_or_404(Book, pk=id)

    return render(request, 'book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling
    })
