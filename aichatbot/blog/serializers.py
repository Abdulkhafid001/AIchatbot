# Blog API models will be serialized(coverted into multiple response types)
from rest_framework import serializers
from blog.models import BlogDb
# authenticated user functionality

# create a class to serialize the blog model
class BlogDbSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = BlogDb
        fields = '__all__'
        read_only_fields = ['author']   