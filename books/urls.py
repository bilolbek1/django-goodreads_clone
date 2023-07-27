from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:id>', BookDetailView.as_view(), name='detail'),
]