from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]


# By Hand


class ProductListAPIViewByHand(APIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        product = self.get_queryset()
        serializer = self.serializer_class(product, many=True)

        return Response(data=serializer.data)

    def get_queryset(self):
        return Product.objects.all().order_by("id")
