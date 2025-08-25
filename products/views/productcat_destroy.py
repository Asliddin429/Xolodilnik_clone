from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import ProductCategory
from products.serializers import ProductCategoryDestroySerializer


class ProductCategoryDestroyAPIView(DestroyAPIView):
    queryset = ProductCategory.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCategoryDestroySerializer
    lookup_field = "id"


# By Hand


class ProductCategoryDestroyAPIViewByHand(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        productcat = self.get_object(id)

        if not productcat:
            return Response(
                data={"detail": "Product category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        productcat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        return ProductCategory.objects.filter(id=id).first()
