from django.contrib import admin
from .models import Post, Comment

# Registering models to the Django Admin site.
# This allows authorized users (superusers) to manage database records via a GUI.

# Basic Registration:
# admin.site.register(Post)
# admin.site.register(Comment)

# --- Professional Approach (Customizing the Admin View) ---

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # This determines which columns are visible in the Admin list view
    list_display = ('title', 'author', 'created_at')
    # Adds a search bar to find posts by title or content
    search_fields = ('title', 'content')
    # Adds a filter sidebar to sort posts by date or author
    list_filter = ('created_at', 'author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at',)