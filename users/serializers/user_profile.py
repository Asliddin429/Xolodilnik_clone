from rest_framework.serializers import ModelSerializer

from users.models import User


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "created_at",
            "updated_at",
        ]
