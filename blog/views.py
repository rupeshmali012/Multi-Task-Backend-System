from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# --- Task 1: Blog & Comment Logic Center ---

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Blog Posts.
    Provides default 'List', 'Create', 'Retrieve', 'Update', and 'Destroy' actions.
    """
    # 1. Queryset: Fetches all post records from the database
    queryset = Post.objects.all()
    
    # 2. Serializer: Maps the model data to JSON format for the API
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling User Comments.
    Automates CRUD operations for the Comment model.
    """
    # Fetches all comment records from the database
    queryset = Comment.objects.all()
    
    # Maps the comment data to JSON format
    serializer_class = CommentSerializer