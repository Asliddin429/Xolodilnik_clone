from rest_framework.serializers import ModelSerializer

from blog.models import Comment


class CommentDetailSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "user", "text", "is_active", "created_at", "updated_at"]
