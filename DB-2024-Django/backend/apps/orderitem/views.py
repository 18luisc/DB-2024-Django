from rest_framework import generics, status
from rest_framework.response import Response

from .models import Orderitem
from .serializer import OrderitemSerializer

class ListCreateOrderitem(generics.ListAPIView):
  queryset = Orderitem.objects.all()
  serializer_class = OrderitemSerializer
  
  def post(self, request, *args, **kwargs):
    data= request.data
    serr = OrderitemSerializer(data=data)
    if (serr.is_valid()):
      serr.save()
      return Response(serr.validated_data, status=status.HTTP_200_OK)  
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
