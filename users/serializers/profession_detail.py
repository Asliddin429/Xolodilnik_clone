from rest_framework.serializers import ModelSerializer

from users.models import Profession


class ProfessionDetailSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = ["id", "name"]
