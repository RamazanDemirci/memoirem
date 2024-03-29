from django.test import Client, TestCase
from django.urls import reverse

from model_mommy import mommy


class TestCaseUtils(TestCase):
    def setUp(self):
        self._user_password = "123456"
        self.user = mommy.prepare("users.User", email="user@email.com")
        self.user.set_password(self._user_password)
        self.user.save()

        self.auth_client = Client()
        self.auth_client.login(email=self.user.email, password=self._user_password)

    def reverse(self, name, *args, **kwargs):
        """Reverse a url, convenience to avoid having to import
        reverse in tests"""
        return reverse(self, name, args=args, kwargs=kwargs)

    def assert_response_200(self, response):
        """ Given response has status_code 200 OK"""
        self.assertEqual(response.status_code, 200)

    def assert_response_201(self, response):
        """ Given response has status_code 201 CREATED"""
        self.assertEqual(response.status_code, 201)

    def assert_response_301(self, response):
        """ Given response has status_code 301 MOVED PERMANENTLY"""
        self.assertEqual(response.status_code, 301)

    def assert_response_302(self, response):
        """ Given response has status_code 302 FOUND"""
        self.assertEqual(response.status_code, 302)

    def assert_response_400(self, response):
        """ Given response has status_code 400 BAD REQUEST"""
        self.assertEqual(response.status_code, 400)

    def assert_response_401(self, response):
        """ Given response has status_code 401 UNAUTHORIZED"""
        self.assertEqual(response.status_code, 401)

    def assert_response_403(self, response):
        """ Given response has status_code 403 FORBIDDEN"""
        self.assertEqual(response.status_code, 403)

    def assert_response_404(self, response):
        """ Given response has status_code 404 NOT FOUND"""
        self.assertEqual(response.status_code, 404)


class TestGetRequiresAuthenticatedUser:
    def test_get_requires_authenticated_user(self):
        response = self.client.get(self.view_url)
        self.assert_response_403(response)


class TestAuthGetRequestSuccess:
    def test_auth_get_success(self):
        response = self.auth_client.get(self.view_url)
        self.assert_response_200(response)
