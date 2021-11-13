from django.shortcuts import render

# Create your views here.


def all_books(request):

    return render(request, 'books/all_books.html')


def book_details(request, book_id):

    return render(request, 'books/book_details.html')
