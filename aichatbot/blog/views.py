from django.contrib.auth.models import User
from blog.serializers import BlogDbSerializer
from blog.models import BlogDb
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.


@api_view(['GET'])
def home(request, format=None):
    return Response()


# using generics viewset
class BlogList(generics.ListCreateAPIView):
    queryset = BlogDb.objects.all()
    serializer = BlogDbSerializer()
    # return Response(serializer.data)

    # function to list blog entries
