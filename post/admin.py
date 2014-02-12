from django.contrib import admin
from post.models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ['dog', 'body', 'post_date']

admin.site.register(Post, PostAdmin)
