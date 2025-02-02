from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer

# A ProfileViewSet
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# V1
class ProfileListView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
