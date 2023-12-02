from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Book, Review
from users.models import CustomUser


class BookTestCase(APITestCase):
    def test_book_list(self):
        book1 = Book.objects.create(title='Mohirdev', description='zo\'r', isbn='12121')
        book2 = Book.objects.create(title='Mohirdev1', description='tavsiya qilaman', isbn='12122')
        book3 = Book.objects.create(title='Mohirdev2', description='mayli', isbn='12123')
        book4 = Book.objects.create(title='Mohirdev3', description='boladi', isbn='12124')
        book5 = Book.objects.create(title='Mohirdev4', description='yaxshi', isbn='12125')

        response = self.client.get(reverse('books_api'))

        self.assertContains(response, book5.title)
        self.assertContains(response, book4.description)
        self.assertContains(response, book3.isbn)
        self.assertContains(response, book2.description)
        self.assertNotContains(response, book1.description)


        response = self.client.get(reverse('books_api') + '?page=2')

        self.assertContains(response, book1.title)
        self.assertContains(response, book1.description)
        self.assertContains(response, book1.isbn)
        self.assertNotContains(response, book4.title)
        self.assertNotContains(response, book3.description)


    def test_book_detail(self):
        book = Book.objects.create(title='Mohirdev', description='jud yaxshi', isbn='12123434')

        response = self.client.get(reverse('book_detail_api', kwargs={'pk': book.pk}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
        self.assertContains(response, book.isbn)



class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(first_name='hunter', username='hunter005')
        self.user.set_password('11223344')
        self.user.save()

        self.book = Book.objects.create(title='title', description='description', isbn='1122')
        self.review = Review.objects.create(star_given=4, review_text="zo'r1", user_id_id=self.user.pk, book_id_id=self.book.pk)
        self.response = self.client.delete(reverse('review_detail_api', kwargs={'pk': self.review.pk}))


        self.client.login(username='hunter005', password='11223344')


    def test_review_list(self):
        book1 = Book.objects.create(title='title', description='description1', isbn='11221')
        book2 = Book.objects.create(title='title1', description='description2', isbn='11222')
        book3 = Book.objects.create(title='title2', description='description3', isbn='11232')
        book4 = Book.objects.create(title='title3', description='description4', isbn='11242')
        book5 = Book.objects.create(title='title4', description='description5', isbn='11252')

        review1 = Review.objects.create(star_given=4, review_text="zo'r1", user_id=self.user, book_id=book1)
        review2 = Review.objects.create(star_given=2, review_text="zo'r2", user_id=self.user, book_id=book2)
        review3 = Review.objects.create(star_given=3, review_text="zo'r3", user_id=self.user, book_id=book3)
        review4 = Review.objects.create(star_given=5, review_text="zo'r4", user_id=self.user, book_id=book4)
        review5 = Review.objects.create(star_given=1, review_text="zo'r5", user_id=self.user, book_id=book5)

        response = self.client.get(reverse('reviews_api'))

        self.assertContains(response, review5.pk)
        self.assertContains(response, review4.star_given)
        self.assertContains(response, review3.user_id.username)
        self.assertContains(response, review3.user_id.first_name)
        self.assertContains(response, review2.user_id.last_name)
        self.assertContains(response, review2.book_id.title)
        self.assertContains(response, review2.book_id.description)
        self.assertNotContains(response, review1.review_text)

        response = self.client.get(reverse('reviews_api') + '?page=2')

        self.assertContains(response, review1.star_given)
        self.assertContains(response, review1.user_id.pk)
        self.assertContains(response, review1.book_id.pk)
        self.assertNotContains(response, review4.review_text)
        self.assertNotContains(response, review2.review_text)
        self.assertNotContains(response, review5.review_text)


    def test_review_delete(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Review.objects.filter(pk=self.review.pk).exists())



    def test_review_patch(self):
        user = CustomUser.objects.create(first_name='hunter', username='hunter55')
        user.set_password('11223344')
        user.save()


        book = Book.objects.create(title='title', description='des', isbn='2321')
        review = Review.objects.create(star_given=5, review_text='review_text', user_id_id=user.pk,
                                        book_id_id=book.pk)
        response = self.client.patch(reverse('review_detail_api', kwargs={'pk': review.pk}),
                                     data={
                                      'star_given': '4',
                                      'review_text': 'salom bu kitob zo\'r ekan'
                                     })
        review.refresh_from_db()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(review.star_given, 4)


    def test_review_put(self):
        user = CustomUser.objects.create(first_name='hunter', username='hunter55')
        user.set_password('11223344')
        user.save()


        book = Book.objects.create(title='title', description='des', isbn='2321')
        review = Review.objects.create(star_given=5, review_text='review_text', user_id_id=user.pk,
                                        book_id_id=book.pk)
        response = self.client.put(reverse('review_detail_api', kwargs={'pk': review.pk}),
                                     data={
                                      'star_given': '4',
                                      'review_text': 'salom bu kitob zo\'r ekan',
                                      'book_id_id': book.pk,
                                      'user_id_id': user.pk
                                     })
        review.refresh_from_db()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(review.star_given, 4)


    def test_review_create(self):
        user = CustomUser.objects.create(first_name='hunter', username='hunter55')
        user.set_password('11223344')
        user.save()

        book = Book.objects.create(title='title', description='des', isbn='2321')


        response = self.client.post(reverse('reviews_api'),
                                    data={
                                        'star_given': '5',
                                        'review_text': 'good book guys',
                                        'book_id_id': book.pk,
                                        'user_id_id': user.pk
                                    })
        review_count = Review.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(review_count, 1)








































































































