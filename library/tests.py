from django.test import TestCase
from library.models import Genre, Book, BorrowedBook, Student
from django.contrib.auth.models import User
import datetime


class BookTestCase(TestCase):
    def setUp(self):
        self.comics = Genre.objects.create(name='Comics')
        self.history = Genre.objects.create(name='History')
        self.book_a = Book.objects.create(isbn_number='ISBN 0001', title='John Doe\'s Book', author='John Doe', genre=self.comics)
        self.student_a = Student.objects.create(adm_number='0001', name='You Know Who', age=23, email='you.know.who@example.com')
        self.student_b = Student.objects.create(adm_number='0002', name='Tom Riddle', age=20)
        self.user = User.objects.create(username='roe', email='roe@example.com', password='secret')

    def test_two_records_created_in_the_table_genres(self):
        self.assertEqual(2, Genre.objects.count())

    def test_book_a_belongs_to_genre_comics(self):
        self.assertTrue(isinstance(self.book_a.genre, Genre))

    def test_students_can_be_added_to_db(self):
        self.assertEqual(2, Student.objects.count())

    def test_can_retrieve_student_records_from_db(self):
        student = Student.objects.filter(adm_number='0001').get()
        self.assertEqual(student.name, self.student_a.name)
        self.assertEqual(student.email, self.student_a.email)

    def test_can_retrieve_only_students_with_email_addresses(self):
        students_with_emails = Student.objects.with_email()
        self.assertEqual(1, students_with_emails.count())
        self.assertIn(self.student_a, students_with_emails)

    def test_students_can_borrow_a_book(self):
        boorrowed_book = BorrowedBook.objects.create(
            book=self.book_a,
            student=self.student_a,
            user=self.user,
            date_borrowed=datetime.datetime.today()
        )
        self.assertEqual(1, BorrowedBook.objects.count())
