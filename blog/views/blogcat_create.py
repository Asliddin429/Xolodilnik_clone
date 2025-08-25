from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogCategory
from blog.serializers import BlogCategoryCreateSerializer


class BlogCategoryCreateAPIView(CreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategoryCreateSerializer
    permission_classes = [IsAuthenticated]


# By Hand
class BlogPostCreateAPIViewyByHand(APIView):
    serializer_class = BlogCategoryCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
