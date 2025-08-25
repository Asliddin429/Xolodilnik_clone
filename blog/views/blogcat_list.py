from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogCategory
from blog.serializers import BlogCategoryListSerializer


class BlogCategoryListAPIView(ListAPIView):
    queryset = BlogCategory.objects.all().order_by("id")
    serializer_class = BlogCategoryListSerializer
    permission_classes = [AllowAny]


# By Hand


class BlogCategoryListAPIViewByHand(APIView):
    serializer_class = BlogCategoryListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        blogcat = self.get_queryset()
        serializer = self.serializer_class(blogcat, many=True)

        return Response(data=serializer.data)

    def get_queryset(self):
        return BlogCategory.objects.all().order_by("id")
