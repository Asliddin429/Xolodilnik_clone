from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Profession
from users.serializers import ProfessionDetailSerializer


class ProfessionDetailAPIView(RetrieveAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# By Hand


class ProfessionDetailAPIViewByHand(APIView):
    serializer_class = ProfessionDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        profession = self.get_object(id)
        serializer = self.serializer_class(profession)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, id):
        return Profession.objects.filter(id=id).first()
