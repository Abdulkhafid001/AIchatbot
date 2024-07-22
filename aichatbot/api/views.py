from rest_framework.response import Response
# used to write the api views
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_data(request):
    person = {"name": "Abdulkhafid"}
    return Response(person)