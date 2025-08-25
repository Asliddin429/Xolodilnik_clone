from rest_framework.serializers import ModelSerializer

from blog.models import BlogCategory


class BlogCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ["name"]
