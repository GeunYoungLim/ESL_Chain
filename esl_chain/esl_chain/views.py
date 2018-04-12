# -*- coding: utf-8 -*-

import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.parsers import JSONParser
from .util import IsValidJSON

# added by GeunYoung Lim 2018. 04. 07
class ESLView(APIView):
    parser_classes = (JSONParser,)

    # hello world example
    def get(self, request):
        content = {'return content': 'hello world'}
        return Response(content)


    # echo example
    def put(self, request):

        # json 입력값 검증
        filter = ['itemId', 'itemName', 'itemPrice', 'itemUrl']
        valid, missing = IsValidJSON(filter, request.data)
        if not valid:
            return Response({'error_msg':'invalid request. you missed ' + missing}, status=status.HTTP_400_BAD_REQUEST)

        #상품 ID ( 나중을 위해 )
        itemId = request.data['itemId']
        #상품 이름
        itemName = request.data['itemName']
        #상품 가격
        itemPrice = request.data['itemPrice']
        #상품 URL
        itemUrl = request.data['itemUrl']



        return Response({'received data': request.data })
