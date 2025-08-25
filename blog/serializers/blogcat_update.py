from rest_framework.serializers import ModelSerializer

from blog.models import BlogCategory


class BlogCategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ["id", "name", "updated_at"]
        read_only_fields = ["id", "updated_at"]
