from rest_framework.serializers import ModelSerializer

from blog.models import BlogPost


class BlogPostDummySerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id"]
