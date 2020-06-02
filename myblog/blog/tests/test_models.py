from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Author, Blog, Comment
import datetime

class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        blog_author = Author.objects.create(user=test_user1, biography='This is a bio')
        blog = Blog.objects.create(blog_title='Test Blog 1',author=blog_author,blog_summary='Test Blog 1 Description')
        
    def test_get_absolute_url(self):
        blog=Blog.objects.get(pk=1)       
        self.assertEquals(blog.get_absolute_url(),'/blog/1')
           
    def test_name_label(self):
        blog=Blog.objects.get(pk=1)
        field_label = blog._meta.get_field('blog_title').verbose_name
        self.assertEquals(field_label,'Blog Title')
        
    def test_name_max_length(self):
        blog=Blog.objects.get(pk=1)
        max_length = blog._meta.get_field('blog_title').max_length
        self.assertEquals(max_length,50)
        
    def test_description_label(self):
        blog=Blog.objects.get(pk=1)
        field_label = blog._meta.get_field('blog_summary').verbose_name
        self.assertEquals(field_label,'Blog Summary')
        
    def test_description_max_length(self):
        blog=Blog.objects.get(pk=1)
        max_length = blog._meta.get_field('blog_summary').max_length
        self.assertEquals(max_length,200)

    def test_date_label(self):
        blog=Blog.objects.get(pk=1)
        field_label = blog._meta.get_field('blog_date').verbose_name
        self.assertEquals(field_label,'Blog Date')

    def test_object_name(self):
        blog=Blog.objects.get(pk=1)
        blog_title = blog.blog_title
        self.assertEquals(blog_title, str(blog))