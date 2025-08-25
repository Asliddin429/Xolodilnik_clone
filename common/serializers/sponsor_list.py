from rest_framework.serializers import ModelSerializer

from common.models import Sponsor


class SponsorListSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["id", "name", "logo", "created_at", "updated_at"]
