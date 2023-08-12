import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView

from .forms import ReviewForm
from .models import Book, AuthorBook, Review


# class BookDetailView(View):
#     def get(self, request, id, review_id):
#         book = Book.objects.get(id=id)
#         author_books = AuthorBook.objects.filter(book=book)
#         review_set = book.review_set.get(id=review_id)
#
#         review = ReviewForm()
#
#         context = {
#             'book': book,
#             'author_books': author_books,
#             'review': review,
#             'review_set': review_set
#         }
#         return render(request, 'book_detail.html', context)


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['author_books'] = AuthorBook.objects.filter(book=book)
        context['review'] = ReviewForm()

        return context


class ReviewView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        review = ReviewForm(data=request.POST)

        if review.is_valid():
            Review.objects.create(
                book_id=book,
                user_id=request.user,
                star_given=review.cleaned_data['star_given'],
                review_text=review.cleaned_data['review_text']

            )
            return redirect(reverse('detail', kwargs={'pk': book.pk}))

        context = {
            'book': book,
            'review': review,
        }
        return render(request, 'book_detail.html', context)





class BookListView(View):
    def get(self, request):
        books = Book.objects.order_by('-id')
        search = request.GET.get('q', '')
        if search:
            books = books.filter(
                Q(title__icontains=search) or Q(description__icontains=search)
            )
            if search not in books:
                messages.info(request, 'The book you are looking for does not exist.')

        if not search and books.count() == 0:
            messages.warning(request, 'There is no books.')

        paginator = Paginator(books, 4)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {
            'books': books,
            'page_obj': page_obj,
        }
        return render(request, 'book_list.html', context)


# class ReviewEditView(UpdateView):
#
#     model = Review
#     template_name = 'update_review.html'
#     context_object_name = 'review_edit'
#
#     def get_context_data(self, review_id, book_id, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['book'] = Book.objects.get(pk=book_id)
#
#         return context



class ReviewEditView(View):
    def get(self, request, book_pk, review_pk):
        book = Book.objects.get(pk=book_pk)
        review = book.review_set.get(pk=review_pk)
        review_form = ReviewForm(instance=review)

        context = {
            'review_form': review_form,
            'book': book,
            'review': review,
        }
        return render(request, 'update_review.html', context)

    def post(self, request, book_pk, review_pk):
        book = Book.objects.get(pk=book_pk)
        review = book.review_set.get(pk=review_pk)
        review_form = ReviewForm(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse('detail', kwargs={'pk': book.pk}))

        else:
            context = {
                'book': book,
                'review': review,
                'review_from': review_form,
            }

            return render(request, 'update_review.html', context)






































