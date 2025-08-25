from rest_framework.serializers import ModelSerializer

from products.models import ProductVariant


class ProductVariantListSerializer(ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "product",
            "name",
            "price",
            "color",
            "size",
            "created_at",
            "updated_at",
        ]
