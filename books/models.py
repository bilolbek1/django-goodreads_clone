from django.db import models


from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


SAVED_TYPE = (
    ('Save', 'Save'),
    ('Saved', 'Saved')
)

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    books_picture = models.ImageField(default='default_book.png')
    pages = models.IntegerField(null=True)
    craeted_time = models.DateTimeField(auto_now_add=True, null=True)
    saved = models.ManyToManyField(CustomUser, default=None, blank=True, related_name='saves')

    def __str__(self):
        return self.title.upper()



class Save(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    value = models.CharField(choices=SAVED_TYPE, max_length=10, default='Save')






class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=128)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AuthorBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Review(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()
    star_given = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    liked = models.ManyToManyField(CustomUser, default=None, blank=True, related_name='likes')

    def __str__(self):
        return self.review_text.capitalize()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)















