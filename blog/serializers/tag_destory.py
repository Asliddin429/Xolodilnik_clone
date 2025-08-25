from rest_framework.serializers import ModelSerializer

from blog.models import Tag


class TagDummySerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id"]
