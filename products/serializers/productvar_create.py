from rest_framework.serializers import ModelSerializer

from products.models import ProductVariant


class ProductVariantCreateSerializer(ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ["product", "name", "price", "color", "size"]
