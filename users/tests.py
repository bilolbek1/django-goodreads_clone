from django.contrib.auth import get_user
from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser


class RegisterTestCase(TestCase):
    def test_create_user(self):
        self.client.post(
            reverse('register'),
            data={
                'username': 'hunter005',
                'first_name': 'Erik',
                'last_name': 'Hunt',
                'email': 'davronm097@gmail.com',
                'password': '12123434'
            }
        )
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)

    def test_username(self):
        user = CustomUser.objects.create_user(username='hunter005', first_name='Bilol')
        user.set_password('12134345')
        user.save()

        response = self.client.post(
            reverse('register'),
            data={
                'username': 'hunter005',
                'first_name': 'Erik',
                'last_name': 'Hunt',
                'email': 'davronm097@gmail.com',
                'password': '12123434'
            }
        )
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')


class LoginTestCase(TestCase):
    def test_login_seccuss(self):
        user = CustomUser.objects.create(username='Hunter', first_name='Jones',
                                         last_name='Bones')
        user.set_password('11112222')
        user.save()

        self.client.post(
            reverse('login'),
            data={
                'username': 'Hunter',
                "password": '11112222',
            }
        )
        new_user = get_user(self.client)
        self.assertTrue(new_user.is_authenticated)

    def test_username_fail(self):
        user = CustomUser.objects.create(username='Hunter', first_name='Jones',
                                         last_name='Bones')
        user.set_password('11112222')
        user.save()

        self.client.post(
            reverse('login'),
            data={
                'username': 'Bilol',
                'password': '11112222',
            }
        )

        new_user = get_user(self.client)
        self.assertFalse(new_user.is_authenticated)


    def test_password_fail(self):
        user = CustomUser.objects.create(username='Hunter', first_name='Jones',
                                         last_name='Bones')
        user.set_password('11112222')
        user.save()

        self.client.post(
            reverse('login'),
            data={
                'username': 'Hunter',
                'password': '11113333',
            }
        )

        new_user = get_user(self.client)
        self.assertFalse(new_user.is_authenticated)

    def test_logout(self):
        user = CustomUser.objects.create(username='Hunter', first_name='Jones',
                                         last_name='Bones')
        user.set_password('11112222')
        user.save()

        self.client.login(username='Hunter', password='11112222')

        self.client.get(reverse('logout'))

        new_user = get_user(self.client)
        self.assertFalse(new_user.is_authenticated)






class ProfileTestCase(TestCase):
    def test_url_profile(self):
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.url, reverse('login') + '?next=/users/profile/')

    def test_profile_details(self):
        user = CustomUser.objects.create(username='Hunter', first_name='Ciryle',
                                         last_name='Gane', email='davronm097@gmail.com')
        user.set_password('11223344')
        user.save()

        self.client.login(username='Hunter', password='11223344')

        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)



































































