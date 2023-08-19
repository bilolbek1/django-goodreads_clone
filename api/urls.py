from django.urls import path

from .views import BookListView, ReviewListView, ReviewDetailView, BookDetailView

urlpatterns =[
    path('books/', BookListView.as_view(), name='books_api'),
    path('reviews/', ReviewListView.as_view(), name='reviews_api'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail_api'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail_api'),
]