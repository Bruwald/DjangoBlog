from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Blog, Theme, Comment
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    biography = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'biography', 'password1', 'password2',)

class BlogForm(ModelForm):
    choices_blog_theme = Theme.objects.all()

    blog_title = forms.CharField(max_length=30, required=True)
    blog_summary = forms.CharField(widget=forms.Textarea)
    blog_theme = forms.ModelChoiceField(queryset=choices_blog_theme, initial=0)
    blog_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_summary', 'blog_theme', 'blog_text',)

class CommentForm(ModelForm):
    comment_text = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Comment
        fields = ('comment_text',)