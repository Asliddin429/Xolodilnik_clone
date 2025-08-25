from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogCategory
from blog.serializers import BlogCategoryUpdateSerializer


class BlogCategroyUpdateAPIView(UpdateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategoryUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


# By Hand


class BlogCategroyUpdateAPIViewByHand(APIView):
    serializer_class = BlogCategoryUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        blogcat = self.get_object(id)
        if not blogcat:
            Response(
                {"detail": "BlogCategory not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(blogcat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, id):
        return BlogCategory.objects.filter(id=id).first()
