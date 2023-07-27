from django.contrib import admin
from .models import Book, AuthorBook, Review, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'isbn']
    search_fields = ['title', 'description', 'isbn']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'bio']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_text', 'star_given']
    search_fields = ['review_text', 'star_given']

class AuthorBookAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']
    search_fields = ['author', 'book']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorBook, AuthorBookAdmin)
admin.site.register(Review, ReviewAdmin)
