from rest_framework.serializers import ModelSerializer

from blog.models import BlogPost


class BlogPostCreateSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "slug",
            "content",
            "image",
            "published_at",
            "user",
            "category",
            "tags",
        ]
        read_only_fields = ["user"]

        def create(self, validated_data):
            request = self.context.get("request")
            if request and hasattr(request, "user"):
                validated_data["user"] = request.user
            return super().create(validated_data)
