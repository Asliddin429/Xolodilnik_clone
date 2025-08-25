from rest_framework.serializers import ModelSerializer

from common.models import Sponsor


class SponsorCreateSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            "name",
            "logo",
        ]
