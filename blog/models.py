from django.db import models
from django.contrib.auth.models import User

# --- Task 1: Blog Management System ---

class Post(models.Model):
    """
    Model representing a Blog Post.
    Each post is authored by a specific User and contains a title and content.
    """
    # Short text field for the post heading
    title = models.CharField(max_length=200)
    
    # Large text field for the blog's body/story
    content = models.TextField()
    
    # Relationship: Each Post belongs to one User (Author). 
    # CASCADE means if the User is deleted, their posts are also removed.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Automatically stores the exact time when the post is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This returns the title instead of 'Post object (1)' in the Admin panel
        return self.title


class Comment(models.Model):
    """
    Model representing user feedback (Comments) on specific blog posts.
    """
    # Relationship: Links this comment to a specific Post.
    # 'related_name' allows us to access comments via post.comments.all()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    
    # Records which registered User made the comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The actual text content of the comment
    text = models.TextField()
    
    # Timestamp for the comment
    created_at = models.DateTimeField(auto_now_add=True)