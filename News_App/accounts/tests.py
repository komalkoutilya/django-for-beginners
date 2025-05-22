from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response=self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code,200)
    
    def test_signup_view_name(self):
        response=self.client.get(reverse("signup"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "registration/signup.html")
    
    def test_signup_form(self):
        response=self.client.post(reverse("signup"),
        {
            "username":"testuser",
            "email":"test@email.com",
            "age":29,
            "password1":"password@149",
            "password2":"password@149",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "test@email.com")
        self.assertEqual(get_user_model().objects.all()[0].age, 29)
        self.assertTrue(get_user_model().objects.all()[0].check_password("password@149"))