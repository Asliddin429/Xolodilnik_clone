from rest_framework.serializers import ModelSerializer

from common.models import Sponsor


class ProductDestroySerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["id"]
