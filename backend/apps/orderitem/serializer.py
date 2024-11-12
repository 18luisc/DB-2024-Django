from rest_framework import serializers
from .models import Orderitem

class OrderitemSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Orderitem
    fields = '__all__'