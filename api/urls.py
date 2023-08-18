from django.urls import path

from .views import BookListView, ReviewListView

urlpatterns =[
    path('books/', BookListView.as_view(), name='books_api'),
    path('reviews/', ReviewListView.as_view(), name='reviews_api'),
]