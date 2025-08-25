from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductDestroySerializer


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductDestroySerializer
    lookup_field = "id"


# By Hand


class ProductDestroyAPIViewByHand(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        product = self.get_object(id)

        if not product:
            return Response(
                data={"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        return Product.objects.filter(id=id).first()
