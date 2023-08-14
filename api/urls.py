from django.urls import path

from api.views import BookReviewDetailView, BookListView

urlpatterns =[
    path('review/<int:pk>/', BookReviewDetailView.as_view(), name='review_detail'),
    path('books/', BookListView.as_view(), name='books'),
]