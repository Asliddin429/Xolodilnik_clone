from rest_framework.serializers import ModelSerializer

from blog.models import Tag


class TagListSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
