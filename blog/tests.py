from django.test import TestCase
from .models import Blog
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        Blog.objects.create(title='my title', body='just a test')
    def test_string_representation(self):
        blog = Blog(title='My entry title')
        self.assertEqual(str(blog), blog.title)
    def test_blog_list_view(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'my title');
        self.assertTemplateUsed(response, 'blog/list.html')
    def test_blog_detail_view(self):
        response = self.client.get('/blog/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'blog/post.html')