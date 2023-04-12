from django.test import TestCase
from .models import Movie, Genre
from captcha.models import CaptchaStore


class URL(TestCase):

    def test_index(self):
        for obj in Movie.objects.all():
            response = self.client.get(f'/movie/{obj.slug}')
            self.assertEqual(response.status_code, 200)
                
    def test_genre(self):
        for obj in Genre.objects.all():
            response = self.client.get(f'/movie/{obj.name}')
            self.assertEqual(response.status_code, 200)

    def test_root(self):
        self.assertEqual(self.client.get('').status_code, 200)

    def test_comment(self):
        """Для неавторизованных пользавателей"""
        for num in range(1, Movie.objects.count()):
            response = self.client.get(f'/movie/review/{num}')
            self.assertEqual(response.status_code, 403)

    def test_user_exit(self):
        user = self.client.login(username='bogdan', password='hflf51423')
        self.assertRedirects(self.client.get('/exit'), '/')










