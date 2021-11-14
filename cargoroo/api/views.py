import math
import urllib.request

from django.contrib.gis.geos import Point
from rest_framework import viewsets, pagination
from rest_framework.decorators import action
from rest_framework.response import Response

from api import models
from api import serializers


class CargorooPagination(pagination.PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data) -> Response:
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

    @action(detail=False, methods=['GET'])
    def nearest(self, request, *args, **kwargs):
        ip_point = self._ip2point()
        if ip_point:
            qs = models.Bike.objects.get_nearest(ip_point)
        else:
            qs = self.get_queryset()

        serializer = serializers.BikeDistanceSerializer(qs, many=True)

        return Response(serializer.data)

    def _determine_ip(self) -> str:
        return urllib.request.urlopen('http://ifconfig.me/ip').read().strip().decode()

    def _ip2point(self) -> Point:
        url = 'https://api.hostip.info/get_html.php?ip={0}&position=true'.format(self._determine_ip())
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/35.0.1916.47 Safari/537.36 '
            }
        )

        f = urllib.request.urlopen(req)
        res = f.read().strip().decode()
        lat, lon = None, None

        for part in res.split('\n'):
            if ':' not in part:
                continue

            key, val = part.split(':')
            if key == 'Latitude':
                lat = val.strip()
            if key == 'Longitude':
                lon = val.strip()

        if lat and lon:
            return Point(float(lon), float(lat), srid=4326)
