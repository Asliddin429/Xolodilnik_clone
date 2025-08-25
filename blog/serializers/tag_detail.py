from rest_framework.serializers import ModelSerializer

from blog.models import Tag


class TagDetailSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
