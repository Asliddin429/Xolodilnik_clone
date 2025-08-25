from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Tag
from blog.serializers import TagDetailSerializer


class TagDetailAPIView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# By Hand


class TagDetailAPIViewByHand(APIView):
    serializer_class = TagDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        tag = self.get_object(id)
        serializer = self.serializer_class(tag)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, id):
        return Tag.objects.filter(id=id).first()
