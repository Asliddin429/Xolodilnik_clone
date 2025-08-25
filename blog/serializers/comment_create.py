from rest_framework.serializers import ModelSerializer

from blog.models import Comment


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post", "text"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["user"] = request.user
        return super().create(validated_data)
