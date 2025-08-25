from rest_framework.serializers import ModelSerializer

from blog.models import BlogCategory


class BlogCategoryDummySerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ["id"]
