from rest_framework.serializers import ModelSerializer

from users.models import Profession


class ProfessionUpdateSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = ["name"]
