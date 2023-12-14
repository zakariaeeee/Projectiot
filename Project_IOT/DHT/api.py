from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Dht11
from .serializers import DHT11serialize

@api_view(["GET", "POST"])
def dhtser(request):
    if request.method == "GET":
        all_data = Dht11.objects.all()
        data_ser = DHT11serialize(all_data, many=True)
        return Response(data_ser.data)
    elif request.method == "POST":
        serial = DHT11serialize(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
