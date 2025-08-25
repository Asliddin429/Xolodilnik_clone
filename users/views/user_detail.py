from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserDetailSerializer


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# By Hand


class UserDetailAPIViewByHand(APIView):
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        user = self.get_object(id)
        serializer = self.serializer_class(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, id):
        return User.objects.filter(id=id).first()
