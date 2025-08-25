from rest_framework.serializers import ModelSerializer

from common.models import Sponsor


class SponsorUpdateSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["id", "name", "logo", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
