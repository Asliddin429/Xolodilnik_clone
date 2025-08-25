from rest_framework.serializers import ModelSerializer

from products.models import ProductCategory


class ProductCategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            "id",
            "name",
            "description",
            "image",
            "is_active",
            "sort_order",
            "created_at",
            "updated_at",
        ]
