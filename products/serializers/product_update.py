from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "image",
            "category",
            "is_featured",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]
