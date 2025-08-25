from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Tag
from blog.serializers import TagDummySerializer


class TagDestroyAPIView(DestroyAPIView):
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TagDummySerializer
    lookup_field = "id"


# By Hand


class TagDestroyAPIViewByHand(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        tag = self.get_object(id)

        if not tag:
            return Response(
                data={"detail": "Tag not found"}, status=status.HTTP_404_NOT_FOUND
            )

        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        return Tag.objects.filter(id=id).first()
