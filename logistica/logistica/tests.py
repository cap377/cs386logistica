from django.test import TestCase
from logistica.views import user_login

# Create your tests here.

class UrlTest1(TestCase):
    def test_fake_url(self):
        resp=self.client.get('/fake/')
        self.assertEqual(resp.status_code, 404)

class UrlTest1(TestCase):
    def test_login_url(self):
        resp=self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

class UrlTest2(TestCase):
    def test_home_url(self):
        resp=self.client.get('/home')
        self.assertEqual(resp.status_code, 200)

class UrlTest3(TestCase):
    def test_loggedin_url(self):
        resp=self.client.get('/loggedin')
        self.assertEqual(resp.status_code, 302)

class UrlTest4(TestCase):
    def test_invalid_url(self):
        resp=self.client.get('/invalid')
        self.assertEqual(resp.status_code, 200)

class UrlTest5(TestCase):
    def test_register_url(self):
        resp=self.client.get('/register/')
        self.assertEqual(resp.status_code, 302)

class UrlTest6(TestCase):
    def test_evaluation_url(self):
        resp=self.client.get('/evaluation')
        self.assertEqual(resp.status_code, 302)


