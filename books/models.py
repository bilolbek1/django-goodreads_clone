from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    isbn = models.CharField(max_length=17)


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=128)
    bio = models.TextField()


class AuthorBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Review(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
    star_given = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])




