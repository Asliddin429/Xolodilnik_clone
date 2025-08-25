from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogPost
from blog.serializers import BlogPostDummySerializer


class BlogPostDestroyAPIView(DestroyAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BlogPostDummySerializer
    lookup_field = "id"


# By Hand


class BlogPostDestroyAPIViewByHand(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        blog = self.get_object(id)

        if not blog:
            return Response(
                data={"detail": "BlogPost not found"}, status=status.HTTP_404_NOT_FOUND
            )

        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        return BlogPost.objects.filter(id=id).first()
