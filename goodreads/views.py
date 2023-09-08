from django.core.paginator import Paginator
from django.shortcuts import render
import datetime
from time import sleep

from books.models import Review, Book


def LandingPageView(request):
    book_last = Book.objects.order_by('-pk')[0]
    books = Book.objects.all().order_by('-pk')[1:5]
    context = {
        'books': books,
        'book_last': book_last
    }
    return render(request, 'landing.html', context)


def HomePageView(request):
    review = Review.objects.order_by('-created_time')

    paginator = Paginator(review, 4)
    pag_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(pag_num)
    context = {
        'review': review,
        'page_obj': page_obj,
    }

    return render(request, 'home.html', context)





















































































