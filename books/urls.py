from django.urls import path
from .views import BookListView, BookDetailView, ReviewView, ReviewUpdateView

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:id>', BookDetailView.as_view(), name='detail'),
    path('<int:id>/review/', ReviewView.as_view(), name='review'),
    path('<int:book_id>/review/<int:review_id>/edit', ReviewUpdateView.as_view(), name='edit_review'),
]