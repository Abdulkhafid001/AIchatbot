from myrestapi.models import Snippet
from myrestapi.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from myrestapi.serializers import UserSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # associating Snippets with Users
    # The way we deal with that is by overriding a .perform_create() method on our snippet views, 
    # that allows us to modify how the instance save is managed, 
    # and handle any information that is implicit in the incoming request or requested URL.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer