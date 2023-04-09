from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view() # by default get present --@api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})


# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'Post request'})


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'this is a Get Request'})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'Post request', 'data':request.data})