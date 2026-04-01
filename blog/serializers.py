from rest_framework import serializers
from .models import Post, Comment

# Serializers define the API representation of our Models.
# They handle both 'Serialization' (Model -> JSON) and 'Deserialization' (JSON -> Model).

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    Converts individual comment database rows into JSON.
    """
    class Meta:
        model = Comment
        # Using '__all__' to include every field from the Comment table
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Blog Post model.
    It includes a nested list of comments for each post.
    """
    # Nested Serialization: This allows us to see all comments belonging to a post
    # 'many=True' means one post can have multiple comments.
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        # Explicitly listing fields to control what data is exposed via the API
        fields = ['id', 'title', 'content', 'author', 'created_at', 'comments']
        
        # Pro-Tip: 'read_only_fields' ensures that the author/timestamp 
        # cannot be manipulated during a POST/PUT request.
        read_only_fields = ['created_at']