import operator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Library,Book
from django.urls  import reverse

def index(request):
    book_list = Library.objects.all()
    context = {'book_list': book_list}
    return render(request, 'library/main.html', context)

def book(request):
    book = Book.objects.all().select_related('library')
    libraries = Library.objects.all()
    librarystr = []
    for d in libraries:
        librarystr.append(d)
    order = {key: i for i, key in enumerate(librarystr)}
    book_list = sorted(book, key=lambda book: order.get(book.library, 0))
    return render(request, 'library/main.html',{'book_list': book_list})

def report(request):
    book = Book.objects.all().select_related('library')
    libraries = Library.objects.all()
    librarystr = []
    for d in book:
        librarystr.append(d)
    order = {key: i for i, key in enumerate(librarystr)}
    book_list = sorted(book, key=lambda book: order.get(book.library, 0))
    return render(request, 'library/view.html',{'book_list': book_list})

def post(request):
    libraries = Library.objects.all().prefetch_related('Post')
    return render(request, 'library/supply.html',{'libraries': libraries})
