from rest_framework.serializers import ModelSerializer

from users.models import Profession


class ProfessionListSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = ["id", "name"]
