from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserProfileSerializer


class UserProfileAPIViewByHand(APIView):
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
