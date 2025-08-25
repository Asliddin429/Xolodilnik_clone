from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Tag
from blog.serializers import TagListSerializer


class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all().order_by("id")
    serializer_class = TagListSerializer
    permission_classes = [AllowAny]


# By Hand
class TagListAPIViewByHand(APIView):
    serializer_class = TagListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        tag = self.get_queryset()
        serializer = self.serializer_class(tag, many=True)

        return Response(data=serializer.data)

    def get_queryset(self):
        return Tag.objects.all().order_by("id")
