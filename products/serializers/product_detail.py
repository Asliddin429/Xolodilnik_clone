from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductDetailSerializer(ModelSerializer):
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
            "created_at",
            "updated_at",
        ]
