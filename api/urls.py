from django.urls import path

from api.views import BookReviewDetailView

urlpatterns =[
    path('review/<int:pk>/', BookReviewDetailView.as_view(), name='review_detail'),
]