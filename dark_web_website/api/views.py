from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from api.models import vehicleStatus
from .serializers import viewVehicleStatusSerializer
from rest_framework.response import Response

class viewVehicleStatusses(generics.ListAPIView):
    serializer_class = viewVehicleStatusSerializer
    queryset = vehicleStatus.objects.all()

class createVehicleStatus(APIView):

    def post(self, request, format=None):
        try:
            payload = request.data[1]["vs"]
            test_1 = request.data('test_1')
            test_2 = request.data('test_2')
            vehicle_name = request.data('vehicle_name')
            vehicleid = request.headers.get('vehicleid')
            vehicle_status = vehicleStatus(vehicleid=vehicleid, payload=payload, test_1=test_1, test_2=test_2, vehicle_name=vehicle_name)
            vehicle_status.save()
            return Response({'Good request': 'saved'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

# class createVehicleStatus(APIView):
#
#     def post(self, request, format=None):
#         try:
#             payload = request.data[1]["vs"]
#
#             # battery_perc = payload[2:4]
#             # battery_perc = int(payload[2:3])-30
#
#             vehicleid = request.headers.get('vehicleid')
#             vehicle_status = vehicleStatus(vehicleid=vehicleid, payload=payload)
#             vehicle_status.save()
#             return Response({'Good request': 'saved'}, status=status.HTTP_201_CREATED)
#         except:
#             return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
