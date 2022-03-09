from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import PostSerializer
from .models import Post

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]