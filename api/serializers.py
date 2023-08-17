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








class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['pk', 'title', 'isbn', 'description', 'books_picture']




class ReviewDetailSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    book_id = BookSerializer(read_only=True)

    user_id_id = serializers.IntegerField(write_only=True)
    book_id_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Review
        fields = ['pk', 'star_given', 'review_text', 'user_id', 'book_id',
                  'book_id_id', 'user_id_id']




























































