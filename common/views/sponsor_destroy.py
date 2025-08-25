from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models import Sponsor
from common.serializers import SponsorDestroySerializer


class SponsorDestroyAPIView(DestroyAPIView):
    queryset = Sponsor.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SponsorDestroySerializer
    lookup_field = "id"


# By Hand


class SponsorDestroyAPIViewByHand(APIView):
    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        sponsor = self.get_object(id)

        if not sponsor:
            return Response(
                data={"detail": "Sponsor not found"}, status=status.HTTP_404_NOT_FOUND
            )

        sponsor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        return Sponsor.objects.filter(id=id).first()
