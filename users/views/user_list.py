from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserListSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]


# By Hand


class UserListAPIViewByHand(APIView):
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        return User.objects.all().order_by("id")
