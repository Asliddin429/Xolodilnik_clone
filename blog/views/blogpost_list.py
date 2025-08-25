from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogPost
from blog.serializers import BlogPostListSerializer


class BlogPostListAPIView(ListAPIView):
    queryset = BlogPost.objects.all().order_by("id")
    serializer_class = BlogPostListSerializer
    permission_classes = [AllowAny]


# By Hand
class BlogPostListAPIViewByHand(APIView):
    serializer_class = BlogPostListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        blog = self.get_queryset()
        serializer = self.serializer_class(blog, many=True)

        return Response(data=serializer.data)

    def get_queryset(self):
        return BlogPost.objects.all().order_by("id")
