from rest_framework.serializers import ModelSerializer

from products.models import ProductVariant


class ProductVariantUpdateSerializer(ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "name",
            "price",
            "color",
            "size",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]
