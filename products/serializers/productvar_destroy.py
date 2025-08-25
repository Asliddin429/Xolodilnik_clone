from rest_framework.serializers import ModelSerializer

from common.models import Sponsor


class ProductVariantDestroySerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["id"]
