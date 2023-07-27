from django.shortcuts import render
from django.views import View
from .models import Book


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {
            'book': book
        }
        return render(request, 'book_detail.html', context)

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            'books': books
        }
        return render(request, 'book_list.html', context)








