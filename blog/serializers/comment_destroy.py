from rest_framework.serializers import ModelSerializer

from blog.models import Comment


class CommentDummySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id"]
