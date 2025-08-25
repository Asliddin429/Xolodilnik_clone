from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductDetailSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# By Hand


class ProductDetailAPIViewByHand(APIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        product = self.get_object(id)
        serializer = self.serializer_class(product)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, id):
        return Product.objects.filter(id=id).first()
