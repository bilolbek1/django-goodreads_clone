from rest_framework import serializers

from books.models import Book, Review
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["pk", 'title', 'isbn', 'description', 'books_picture']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["pk", 'first_name', 'last_name', 'username', 'email']



class ReviewSerializer(serializers.ModelSerializer):

    # REVIEW LIST BO'LIB CHIQAYOTGANDA UNING USERI VA BOOKI HAM CHIQISHI UCHUN YARATILDI

    book_id = BookSerializer(read_only=True)
    user_id = UserSerializer(read_only=True)

    # REVIEW YARATAYOTGANIMIZDA QAYSI KITOBGA VA QAYSI USERDAN EKANLIGINI ANIQLASH UCHUN KERAK BO'LDI,
    # CHUNKI DJANGODAGI CODIMIZDA HAM USHBU FIELDLAR BO'LADI FAQAT UNDA AVTOMAYIK TO'LDIRILGAN

    book_id_id = serializers.IntegerField(write_only=True)
    user_id_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Review
        fields = ["pk", 'star_given', 'review_text', 'user_id', 'book_id', 'book_id_id', 'user_id_id']






















































