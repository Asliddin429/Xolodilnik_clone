from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogCategory
from blog.serializers import BlogCategoryDetailSerializer


class BlogCategoryDestroyAPIView(DestroyAPIView):
    queryset = BlogCategory.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BlogCategoryDetailSerializer
    lookup_field = "id"


# By Hand


class BlogCategoryDestroyAPIViewByHand(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        blogcat = self.get_object(id)

        if not blogcat:
            return Response(
                data={"detail": "Blog category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        blogcat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        return BlogCategory.objects.filter(id=id).first()
