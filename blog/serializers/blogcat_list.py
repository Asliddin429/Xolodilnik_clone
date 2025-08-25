from rest_framework.serializers import ModelSerializer

from blog.models import BlogCategory


class BlogCategoryListSerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ["id", "name", "is_active", "created_at", "updated_at"]
