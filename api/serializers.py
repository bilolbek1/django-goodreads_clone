from rest_framework import serializers

from books.models import Book, Review
from users.models import CustomUser




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk', 'first_name', 'last_name', 'username', 'email']



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['pk', 'title', 'description', 'isbn']




class ReviewDetailSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    book_id = BookSerializer()
    class Meta:
        model = Review
        fields = ['pk', 'star_given', 'review_text', 'user_id', 'book_id']
