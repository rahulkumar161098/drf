import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def homeApi(request, *args, **kwargs):
    body= request.body
    print(request.GET)
    print(request.POST)
    data={}
    try:
      data= json.loads(body)
      print(data)
    except:
       pass
    print(data)
    print(request.headers)
    print(request.content_type)
    return JsonResponse({'message':'Hi there, I am api from Django'})