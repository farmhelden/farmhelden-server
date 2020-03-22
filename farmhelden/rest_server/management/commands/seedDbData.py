from django.core.management.base import BaseCommand, CommandError
from rest_server.models import User, Farm, Location, Campaign
from django.utils import timezone
from django.contrib.gis.geos import Point

import datetime

import pytz


class Command(BaseCommand):

    def handle(self, *args, **options):
        start = pytz.utc.localize(datetime.datetime(2020, 5, 1, 0, 0))
        end = pytz.utc.localize(datetime.datetime(2020, 5, 5, 0, 0))
        self.create_users_with_farms_locations_and_campaign(email="foo@bar.com", password="password",
                                                 street="Am Deich 2", zip_code="25797",
                                                 info="Hof Haase", date_from=start, date_to=end, point=Point(9.010076, 54.144092))

    def create_users_with_farms_locations_and_campaign(self, email, password, street, zip_code, info, date_from,
                                                       date_to, point, location_type=1):
        try:
            user = User.objects.get(email=email)
        except:
            user = User.objects.create(email=email, password=password)

        farm = Farm.objects.create(street=street, zip_code=zip_code, user_id=user)
        location = Location.objects.create(info=info, farm_id=farm, location_type=location_type, point=point)

        self.create_campaign(farm=farm, location=location, date_from=date_from, date_to=date_to)

        return user, farm, location

    def create_campaign(farm, location, date_from, date_to):
        campaign = Campaign.objects.create(farm_id=farm, location_id=location, date_from=date_from, date_to=date_to)
        return campaign
