from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models import Sponsor
from common.serializers import SponsorUpdateSerializer


class SponsorUpdateAPIView(UpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


# By Hand


class SponsorUpdateAPIViewByHand(APIView):
    serializer_class = SponsorUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        sponsor = self.get_object(id)

        if not sponsor:
            return Response(
                {"detail": "Sponsor not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(data=request.data, instance=sponsor)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, id):
        return Sponsor.objects.filter(id=id).first()
