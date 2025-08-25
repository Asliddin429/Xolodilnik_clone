from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Profession
from users.serializers import ProfessionDestroySerializer


class ProfessionDestroyAPIView(DestroyAPIView):
    queryset = Profession.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfessionDestroySerializer
    lookup_field = "id"


# By Hand


class ProfessionDestroyAPIViewByHand(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        profession = self.get_object(id)
        if not profession:
            return Response(
                data={"detail": "Profession not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        profession.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        return Profession.objects.filter(id=id).first()
