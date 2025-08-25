from rest_framework.serializers import ModelSerializer

from blog.models import Tag


class TagUpdateSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
        read_only_fields = ["id"]
