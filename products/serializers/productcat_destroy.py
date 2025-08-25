from rest_framework.serializers import ModelSerializer

from common.models import Sponsor


class ProductCategoryDestroySerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["id"]
