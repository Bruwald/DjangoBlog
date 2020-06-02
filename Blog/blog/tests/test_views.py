from django.test import TestCase
from blog.models import Blog, Author
from django.urls import reverse
from django.contrib.auth.models import User

class BlogListView(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        blog_author = Author.objects.create(user=test_user1, biography='This is a bio')
        
        number_of_blogs = 13
        for blog_num in range(number_of_blogs):
           Blog.objects.create(blog_title='Test Blog %s' % blog_num,author=blog_author,blog_summary='Test Blog %s Description' % blog_num)
    
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/blog/blogs/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blogs.html')