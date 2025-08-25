from rest_framework.serializers import ModelSerializer

from users.models import Profession


class ProfessionDestroySerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = ["id"]
