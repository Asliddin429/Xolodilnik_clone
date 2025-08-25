from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import ProductVariant
from products.serializers import ProductVariantDetailSerializer


class ProductVarinatDetailAPIView(RetrieveAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# By Hand


class ProductVariantDetailAPIViewByHand(APIView):
    serializer_class = ProductVariantDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        productvar = self.get_object(id)
        serializer = self.serializer_class(productvar)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, id):
        return ProductVariant.objects.filter(id=id).first()
