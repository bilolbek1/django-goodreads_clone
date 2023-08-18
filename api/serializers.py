from rest_framework import serializers

from books.models import Book, Review
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description', 'books_picture']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']



class ReviewSerializer(serializers.ModelSerializer):
    book_id = BookSerializer()
    user_id = UserSerializer()
    class Meta:
        model = Review
        fields = ('star_given', 'review_text', 'user_id', 'book_id')






















































