from django.contrib import admin
from .models import Post,Library,Book


admin.site.register(Library)

admin.site.register(Book)

admin.site.register(Post)
# Register your models here.
