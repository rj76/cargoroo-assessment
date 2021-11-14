import math
from rest_framework import viewsets, pagination
from rest_framework.response import Response

from api import models
from api import serializers


class CargorooPagination(pagination.PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'num_pages': math.ceil(self.page.paginator.count / self.page_size),
            'results': data,
        })


class FleetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FleetSerializer
    queryset = models.Fleet.objects.all()
    pagination_class = CargorooPagination


class BikeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BikeSerializer
    queryset = models.Bike.objects.all()
    pagination_class = CargorooPagination
