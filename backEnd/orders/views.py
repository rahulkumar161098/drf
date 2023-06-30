from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Orders
from . import serializers

# Create your views here.
class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'message': 'Hello Order'}, status=status.HTTP_200_OK)
    
class OrderCreationView(generics.GenericAPIView):

    serializer_class= serializers.OrderSerializer
    queryset= Orders.objects.all()

    def get(self, request):
        orders= Orders.objects.all()
        serializer= self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status= status.HTTP_200_OK)
        


    def post(self, request):
        pass


class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        pass

    def put(self, request, order_id):
        pass

    def delete(self, request, order_id):
        pass

