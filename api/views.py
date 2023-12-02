from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookSerializer, ReviewSerializer
from books.models import Book, Review


# KITOBLAR LIST BO'LIB CHIQISHI UCHUN YOZILGAN VIEW

class BookListView(LoginRequiredMixin, APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        books = Book.objects.all().order_by('-pk')
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(page_obj, many=True)


        return paginator.get_paginated_response(serializer.data)



# KITOBLARNI DETALNI QILIB CHIQISHI UCHUN VIEW


class BookDetailView(LoginRequiredMixin, APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)

        return Response(serializer.data)





# REVIEWLAR LIST BO'LIB CHIQISHI UCHUN YOZILGAN VIEW
class ReviewListView(LoginRequiredMixin, APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        reviews = Review.objects.all().order_by('-pk')
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(reviews, request)
        serializer = ReviewSerializer(page_obj, many=True)

        return paginator.get_paginated_response(serializer.data)


    def post(self, request):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# REVIEW DETAIL UCHUN YOZILGAN VIEW
class ReviewDetailView(LoginRequiredMixin, APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)

        return Response(serializer.data)


    def delete(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(instance=review, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(instance=review, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

















































