from rest_framework import routers

from . import views


api = routers.SimpleRouter()
api.register(r'fleet', views.FleetViewSet)
api.register(r'bike', views.BikeViewSet)
