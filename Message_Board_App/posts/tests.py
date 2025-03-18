from django.test import TestCase
from django.urls import reverse
from .models import Posts

# Create your tests here.
class PostsTestCase(TestCase):
    @classmethod
    # set up the test data
    def setUpTestData(cls):
        cls.post = Posts.objects.create(text="This is a test!")
    
    # test the model content
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test!")