from rest_framework.serializers import ModelSerializer

from common.models import Sponsor


class SponsorDestroySerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["id"]
