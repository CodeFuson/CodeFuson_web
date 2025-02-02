from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from .models import Profile  # Feltételezve, hogy van ilyen modelled
from .serializers import ProfileSerializer

# DRF ViewSet a profilokhoz
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Alternatív, ha sima APIView kell
class ProfileListCreateView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
