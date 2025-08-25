from rest_framework.serializers import ModelSerializer

from blog.models import BlogPost


class BlogPostDetailSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "status",
            "is_featured",
            "published_at",
            "created_at",
            "updated_at",
            "user",
            "category",
            "tags",
        ]
