from myrestapi.models import Snippet
from myrestapi.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from myrestapi.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myrestapi.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets

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


# use the DRF viewsets to create a viewset that uses routers to reduce code for views
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


# using the DRF reverse function to return fully-qualified URLs;
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
