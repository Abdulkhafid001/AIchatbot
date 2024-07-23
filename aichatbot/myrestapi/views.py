from myrestapi.models import Snippet
from myrestapi.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from myrestapi.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.response import Response
from myrestapi.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse

# using the DRF permissions class
permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # associating Snippets with Users
    # this method is always called when a serializer is created
    # so we pass a snippet owner to the serializer everytime a new snippet is created
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# using the DRF permissions class
permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
