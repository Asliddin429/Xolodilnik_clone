from rest_framework.serializers import ModelSerializer

from products.models import ProductCategory


class ProductCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["name", "description", "image"]
