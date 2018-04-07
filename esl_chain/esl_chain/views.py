import json

from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.parsers import JSONParser
# added by GeunYoung Lim 2018. 04. 07
class ExampleView(APIView):
    parser_classes = (JSONParser,)

    # hello world example
    def get(self, request):
        content = {'return content': 'hello world'}
        return Response(content)


    # echo example
    def post(self, request):
        return Response({'received data': request.data })
