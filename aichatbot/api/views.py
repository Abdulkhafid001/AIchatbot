from django.contrib.auth.models import Group, User
from rest_framework.response import Response
# used to write the api views
from rest_framework.decorators import api_view, permissions, viewsets
# get serializers to convert model db types to python primitive types
from .serializers import UserSerializer, GroupSerializer
from myrestapi.models import Item

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]