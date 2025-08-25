from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from products.models import ProductCategory
from products.serializers import ProductCategoryListSerializer


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.all().order_by("id")
    serializer_class = ProductCategoryListSerializer
    permission_classes = [AllowAny]


# By Hand


class ProductCategoryListAPIViewByHand(APIView):
    serializer_class = ProductCategoryListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        productcat = self.get_queryset()
        serializer = self.serializer_class(productcat, many=True)

    def get_queryset(self):
        return ProductCategory.objects.all().order_by("id")
