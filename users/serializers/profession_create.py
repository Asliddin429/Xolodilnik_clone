from rest_framework.serializers import ModelSerializer

from users.models import Profession


class ProfessionCreateSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = ["name"]
