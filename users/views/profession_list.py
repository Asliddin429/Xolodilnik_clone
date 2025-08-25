from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Profession
from users.serializers import ProfessionListSerializer


class ProfessionListAPIView(ListAPIView):
    queryset = Profession.objects.all().order_by("id")
    serializer_class = ProfessionListSerializer
    permission_classes = [AllowAny]


# By Hand


class ProfessionListAPIViewByHand(APIView):
    serializer_class = ProfessionListSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        profession = self.get_queryset()
        serializer = self.serializer_class(profession, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Profession.objects.all().order_by("id")
