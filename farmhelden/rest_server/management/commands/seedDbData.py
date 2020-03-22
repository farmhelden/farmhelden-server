from django.core.management.base import BaseCommand, CommandError
from rest_server.models import User, Farm, Location, Campaign
import datetime

import pytz

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            myUser = User.objects.get(email="foo@bar.com")
        except:
            myUser = User.objects.create(email="foo@bar.com", password="password")

        myFarm = Farm.objects.create(street="Bahnhofstrasse 22", zip_code="12345", user_id=myUser)
        myLocation = Location.objects.create(info="Ein schöner ort", farm_id=myFarm, location_type=1)

        start = pytz.utc.localize(datetime.datetime(2020, 5, 1, 0, 0))
        end = pytz.utc.localize(datetime.datetime(2020, 5, 5, 0, 0))
        myCampaign = Campaign.objects.create(farm_id=myFarm, location_id=myLocation, date_from=start, date_to=end)
