from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import ProductVariant
from products.serializers import ProductVariantListSerializer


class ProductVariantListAPIView(ListAPIView):
    queryset = ProductVariant.objects.all().order_by("id")
    serializer_class = ProductVariantListSerializer
    permission_classes = [AllowAny]


# By Hand


class ProductVariantListAPIView(APIView):
    serializer_class = ProductVariantListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        productvar = self.get_queryset()
        serializer = self.serializer_class(productvar, many=True)

        return Response(data=serializer.data)

    def get_queryset(self):
        return ProductVariant.objects.all().order_by("id")
