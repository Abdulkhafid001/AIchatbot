from rest_framework.response import Response
# used to write the api views
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from myrestapi.models import Item
# from  import ItemSerializer
@api_view(['GET'])
def get_data(request):
    # get all database data
    items = Item.objects.all()
    # serialize to json
    serializer = ItemSerializer(items)
    return Response(serializer.data)