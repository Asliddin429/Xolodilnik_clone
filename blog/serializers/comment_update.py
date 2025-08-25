from rest_framework.serializers import ModelSerializer

from blog.models import Comment


class CommentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text", "updated_at"]
        read_only_fields = ["id", "updated_at"]

    def update(self, instance, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            instance.user = request.user
        return super().update(instance, validated_data)
