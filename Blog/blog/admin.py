from django.contrib import admin
from blog.models import Author, Blog, Theme

# Register your models here.
admin.site.register(Author)
admin.site.register(Theme)
admin.site.register(Blog)
