import json
from pathlib import Path

from django.contrib.gis.geos import Point

from api import models


class Batch:
    def run(self):
        datafile = '{0}/data.json'.format(Path(__file__).parent.parent.parent)

        with open(datafile) as f:
            models.Fleet.objects.all().delete()
            d = json.load(f)

            for fleet_dict in d['fleets']:
                models.Fleet.objects.create(**fleet_dict)

            for bike_dict in d['bikes']:
                bike_dict['fleet'] = models.Fleet.objects.get(id=bike_dict['fleet'])
                bike_dict['location'] = Point(
                    bike_dict['location']['longitude'],
                    bike_dict['location']['latitude']
                )

                models.Bike.objects.create(**bike_dict)
