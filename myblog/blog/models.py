from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Blog(models.Model):
    
    blog_title = models.CharField('Blog Title', max_length=50, help_text = "Enter your Blog Title")
    blog_text = models.TextField('Blog Text', help_text = "Enter your Blog Text")
    blog_summary = models.CharField('Blog Summary', max_length=200, help_text = 'Enter your Blog Summary', null=True, blank=True)
    blog_theme = models.ForeignKey('Theme', null=True, on_delete=models.SET_NULL, help_text = "Enter your Blog Theme")
    blog_date = models.DateTimeField('Blog Date', auto_now_add = True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['blog_theme','-blog_date']

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.id)])

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=50, help_text = 'Enter your First Name')
    last_name = models.CharField('Last Name', max_length=50, help_text = 'Enter your Last Name')
    biography = models.TextField('Biography', max_length=300, help_text = 'Enter your Biography', null=True, blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])

class Theme(models.Model):

    theme = models.CharField('Theme', max_length=50, help_text = "Enter your Theme")

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'
        ordering = ['theme']

    def __str__(self):
        return f'{self.theme}'

    def get_absolute_url(self):
        return reverse('theme-detail', args=[str(self.id)])

class Comment(models.Model):

    comment = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ["comment_date"]

    def __str__(self):
        return f'{self.comment}'
    
    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])