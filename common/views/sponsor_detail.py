from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models import Sponsor
from common.serializers import SponsorDetailSerializer


class SponsorDetailAPIView(RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# By Hand


class SponsorDetailAPIViewByHand(APIView):
    serializer_class = SponsorDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        sponsor = self.get_object(id)
        serializer = self.serializer_class(sponsor)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_object(self, id):
        return Sponsor.objects.filter(id=id).first()
