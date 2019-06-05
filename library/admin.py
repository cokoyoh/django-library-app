from django.contrib import admin
from .models import Student, Genre, Book, Reservation, BorrowedBook


admin.site.register(Student)
admin.site.register(Genre)
admin.site.register(Reservation)
admin.site.register(BorrowedBook)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre')
