from django.contrib import admin
from .models import Blog, Comment
# Register your models here.
class CommentInline(admin.TabularInline): # admin.TabularInline is used for showing the comments in the same page as the blog
    model = Comment
    extra = 0
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title', 'body']
    inlines = [CommentInline]
admin.site.register(Blog, BlogAdmin)