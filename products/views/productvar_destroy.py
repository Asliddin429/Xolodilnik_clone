from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import ProductVariant
from products.serializers import ProductVariantDestroySerializer


class ProductVariantDestroyAPiView(DestroyAPIView):
    queryset = ProductVariant.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductVariantDestroySerializer
    lookup_field = "id"


# By Hand


class ProductVariantDestroyAPIViewByHand(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        productvar = self.get_object(id)

        if not productvar:
            return Response(
                data={"detail": "Product variant not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        productvar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        return ProductVariant.objects.filter(id=id).first()
