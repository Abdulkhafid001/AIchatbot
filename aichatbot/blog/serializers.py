# Blog API models will be serialized(coverted into multiple response types)
from rest_framework import serializers
from blog.models import Blog_DB
# authenticated user functionality

# create a class to serialize the blog model
class BlogDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_DB
        fields = '__all__'