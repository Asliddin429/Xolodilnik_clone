from rest_framework.serializers import ModelSerializer

from products.models import ProductCategory


class ProductCategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            "id",
            "name",
            "description",
            "image",
            "is_active",
            "sort_order",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]
