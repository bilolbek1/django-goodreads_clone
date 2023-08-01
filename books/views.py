from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

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
        books = Book.objects.order_by('id')
        search = request.GET.get('q', '')
        if search:
            books = books.filter(
                Q(title__icontains=search) or Q(description__icontains=search)
            )

        if books.count() == 0:
            messages.warning(request, 'There is no books')

        paginator = Paginator(books, 4)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'books': books,
            'page_obj': page_obj,
        }
        return render(request, 'book_list.html', context)









