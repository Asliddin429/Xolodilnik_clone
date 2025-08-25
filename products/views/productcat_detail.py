from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import ProductCategory
from products.serializers import ProductCategoryDetailSerializer


class ProductCategoryDetailAPIView(RetrieveAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# By Hand


class ProductCategoryDetailAPIViewByHand(APIView):
    serializer_class = ProductCategoryDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        productcat = self.get_object(id)
        serializer = self.serializer_class(productcat)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, id):
        return ProductCategory.objects.filter(id=id).first()
