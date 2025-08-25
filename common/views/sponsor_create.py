from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models import Sponsor
from common.serializers import SponsorCreateSerializer


class SponsorCreateAPIView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer
    permission_classes = [IsAuthenticated]


# By Hand


class SponsorCreateAPIViewByHand(APIView):
    serializer_class = SponsorCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, requst, *args, **kwargs):
        serializer = self.serializer_class(data=requst.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
