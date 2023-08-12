from django.urls import path
from .views import BookListView, BookDetailView, ReviewView, ReviewEditView

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:pk>', BookDetailView.as_view(), name='detail'),
    path('<int:pk>/review/', ReviewView.as_view(), name='review'),
    path('<int:book_pk>/review/<int:review_pk>/edit/', ReviewEditView.as_view(), name='review_edit'),
]