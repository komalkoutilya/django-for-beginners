from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post
# Create your tests here.

# 1.Set up Test DataBase and assertEach Field
# 2.Test urls exists at correct location
# 3.Test Blog_List_View and Blog_Detail_View

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user=get_user_model().objects.create_user(username="testuser", email="test@email.com",password="secret")

        cls.post=Post.objects.create(title="TestPost", author=cls.user, body="This is a Test Blog")
    
    def test_post_model(self):
        self.assertEqual(self.user.username,"testuser")
        self.assertEqual(self.user.email,"test@email.com")
        self.assertTrue(self.user.check_password("secret")) #passwords can't be assertEqual because they are Hased using SHA-256

        self.assertEqual(self.post.title,"TestPost")
        self.assertEqual(self.post.author.username,"testuser")
        self.assertEqual(self.post.body,"This is a Test Blog")
        self.assertEqual(str(self.post),"TestPost")
        self.assertEqual(self.post.get_absolute_url(),"/post/1/")

    def test_url_exists_at_correct_location_blog_list_view(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)
    
    def test_url_exists_at_correct_location_blog_detail_view(self):
        response=self.client.get("/post/1/")
        self.assertEqual(response.status_code,200)
    
    def test_blog_list_view(self):
        response=self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"home.html")
        self.assertContains(response,self.post.title) # blog-titles-loaded
        self.assertContains(response,self.post.body) # blog-contents-loaded
        self.assertContains(response,"Django Blogs") # heading-loaded
    
    def test_blog_detail_view(self):
        response=self.client.get(reverse("post_detail",kwargs={"pk":self.post.pk}))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"post_detail_view.html")
        self.assertContains(response,self.post.title) # specific-blog-title-loaded
        self.assertContains(response,self.post.body) # specific-blog-body-loaded
        self.assertContains(response,"Django Blogs") # heading-loaded

        no_response=self.client.get("/post/1000/") #post-doesn't exists
        self.assertEqual(no_response.status_code,404) #status not found error