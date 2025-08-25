from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Comment
from blog.serializers import CommentDummySerializer


class CommentDestroyAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentDummySerializer
    lookup_field = "id"


# By Hand


class CommentDestroyAPIViewByHand(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        comment = self.get_object(id)

        if not comment:
            return Response(
                data={"detail": "Comment not found"}, status=status.HTTP_404_NOT_FOUND
            )

        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        return Comment.objects.filter(id=id).first()
