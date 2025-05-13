from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class AccountsTest(TestCase):
    def test_signup_page_status_code(self):
        """
        Tests if the signup page returns a 200 OK status code.
        """
        url = reverse("signup")
        response = self.client.get(url)
        return self.assertEqual(response.status_code, 200)
    
    def test_login_page_status_code(self):
        """
        Tests if the login page returns a 200 OK status code.
        """
        url = reverse("login")
        response = self.client.get(url)
        return self.assertEqual(response.status_code, 200)