from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class ArtistList(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
