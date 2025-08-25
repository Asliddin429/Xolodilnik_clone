from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Comment
from blog.serializers import CommentListSerializer


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all().order_by("id")
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]


# By Hand
class CommentListAPIViewByHand(APIView):
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        comment = self.get_queryset()
        serializer = self.serializer_class(comment, many=True)

        return Response(data=serializer.data)

    def get_queryset(self):
        return Comment.objects.all().order_by("id")
