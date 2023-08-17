from django.urls import path

from api.views import BookReviewDetailView, BookListView, ReviewsView

urlpatterns =[
    path('reviews/<int:pk>/', BookReviewDetailView.as_view(), name='review_detail'),
    path('books/', BookListView.as_view(), name='books'),
    path('reviews/', ReviewsView.as_view(), name='reviews'),
]