from .models import Orders
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    
    size= serializers.CharField(max_length=20)
    status= serializers.HiddenField(default='PENDING')
    quantity= serializers.IntegerField()

    class Meta:
        model = Orders
        fields= ['size', 'status', 'quantity']