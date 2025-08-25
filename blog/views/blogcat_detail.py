from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogCategory
from blog.serializers import BlogCategoryDetailSerializer


class BlogCategoryDetailAPIView(RetrieveAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategoryDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# By Hand


class BlogCategoryDetailAPIViewByHand(APIView):
    serializer_class = BlogCategoryDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        blogcat = self.get_object(id)
        serializer = self.serializer_class(blogcat)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, id):
        return BlogCategory.objects.filter(id=id).first()
