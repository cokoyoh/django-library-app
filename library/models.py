from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Student(models.Model):
    adm_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'students'
        ordering = ['adm_number']

    def __str__(self):
        return '{0} - {1}'.format(self.adm_number, self.name)


class Genre(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'genres'
        ordering = ['created_at']

    def __str__(self):
        return '{0}'.format(self.name)


class BooksQuerySet(models.QuerySet):
    def borrowed_books(self):
        return self.filter(borrows__isnull=False)


class Book(models.Model):
    isbn_number = models.CharField(max_length=45, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    objects = BooksQuerySet.as_manager()

    class Meta:
        db_table = 'books'
        ordering = ['-isbn_number']

    def __str__(self):
        return '{0} - {1} By {2}'.format(self.isbn_number, self.title, self.author)


class ReservationQuerySet(models.QuerySet):
    def reserved_today(self):
        return self.filter(created_at__date=date.today())


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='reservations')
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    issued_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    objects = ReservationQuerySet.as_manager()

    class Meta:
        db_table = 'book_reservations'
        ordering = ['-created_at']

    def __str__(self):
        return '{0} reserved for {1}'.format(self.book.title, self.student.name)


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='borrows')
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='borrows')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_borrowed = models.DateField()
    date_returned = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'borrowed_books'
        ordering = ['-created_at']

    def __str__(self):
        return '{0} borrowed by {1}'.format(self.book.title, self.student.name)
