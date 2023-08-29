from django.urls import path
from .views import BookListView, BookDetailView, ReviewView, ReviewDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:pk>', BookDetailView.as_view(), name='detail'),
    path('<int:pk>/review/', ReviewView.as_view(), name='review'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail')
]