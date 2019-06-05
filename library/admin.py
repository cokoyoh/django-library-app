from django.contrib import admin
from .models import Student, Genre, Book, Reservation, BorrowedBook


# admin.site.register(Student)
admin.site.register(Genre)
admin.site.register(Reservation)
# admin.site.register(BorrowedBook)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('adm_number', 'name', 'email', 'age')


@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'student', 'date_borrowed', 'date_returned', 'user')
    list_editable = ('date_borrowed',)
