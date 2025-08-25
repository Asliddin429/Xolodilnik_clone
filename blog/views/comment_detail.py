from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Comment
from blog.serializers import CommentDetailSerializer


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# By Hand


class CommentDetailAPIViewByHand(APIView):
    serializer_class = CommentDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        comment = self.get_object(id)
        serializer = self.serializer_class(comment)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, id):
        return Comment.objects.filter(id=id).first()
