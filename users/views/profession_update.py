from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Profession
from users.serializers import ProfessionUpdateSerializer


class ProfessionUpdateAPIView(UpdateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


# By Hand


class ProfessionUpdateAPIViewByHand(APIView):
    serializer_class = ProfessionUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        profession = self.get_object(id)

        if not profession:
            return Response(
                {"detail": "Profession not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(data=request.data, instance=profession)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, id):
        return Profession.objects.filter(id=id).first()
