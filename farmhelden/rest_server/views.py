from rest_framework import viewsets
from rest_framework import permissions
from rest_server.models import Farm, User
from rest_server.serializers import UserSerializer, FarmSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]
