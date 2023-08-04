from django.core.paginator import Paginator
from django.shortcuts import render
import datetime
from time import sleep

from books.models import Review


def LandingPageView(request):
    return render(request, 'landing.html')


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





















































































