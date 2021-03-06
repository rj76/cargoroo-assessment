from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from . import models


class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fleet
        fields = ('id', 'name')


class BikeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Bike
        geo_field = 'location'
        fields = ('id', 'fleet', 'status', 'location')


class BikeDistanceSerializer(GeoFeatureModelSerializer):
    distance = serializers.SerializerMethodField()

    def get_distance(self, obj):
        if hasattr(obj, 'distance'):
            return obj.distance.km

        return 0

    class Meta:
        model = models.Bike
        geo_field = 'location'
        fields = ('id', 'fleet', 'status', 'location', 'distance')
