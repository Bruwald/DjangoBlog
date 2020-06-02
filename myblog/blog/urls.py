from django.urls import include, path
from django.views.generic.base import RedirectView
from blog import views

urlpatterns = [
    path('', RedirectView.as_view(url='blogs/')),
    path('blogs/', views.blogs, name='blogs'),
    path('<int:primaryKey>', views.blog, name='blog-detail'),
    path('author/<int:primaryKey>', views.author, name='author-detail'),
    path('myposts', views.myposts, name='myposts'),
    path('newpost', views.newpost, name='newpost'),
    path('postcomment/<int:blog_pk>', views.postcomment, name='postcomment'),
]