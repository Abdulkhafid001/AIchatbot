# Serializers take querysets and model instances and convert them into native Python data types.
# We can then take those data types and render them into JSON.
from rest_framework import serializers

from django.contrib.auth.models import Group, User


# user serializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# group user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
