from rest_framework.serializers import ModelSerializer

from blog.models import Tag


class TagCreateSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]
