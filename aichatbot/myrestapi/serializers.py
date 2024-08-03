from rest_framework import serializers
from myrestapi.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlighted = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='HTML')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'linenos',
                  'language', 'style', 'owner', 'highlighted']

# this user serializer get all the user and they snippets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']      
