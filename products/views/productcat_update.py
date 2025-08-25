from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import ProductCategory
from products.serializers import ProductCategoryUpdateSerializer


class ProductCategoryUpdateAPIView(UpdateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


# By Hand


class ProductCategoryUpdateAPIViewByHand(APIView):
    serializer_class = ProductCategoryUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        productcat = self.get_object(id)
        if not productcat:
            return Response(
                {"detail": "Product category not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(data=request.data, instance=productcat)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, id):
        return ProductCategory.objects.filter(id=id).first()
