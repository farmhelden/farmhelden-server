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
        self.create_users_with_farms_locations_and_campaign(email="foo1@bar.com", password="password",
                                                 street="Am Deich 2", zip_code="25797",
                                                 info="Hof Haase", date_from=start, date_to=end, point=Point(9.010076, 54.144092))

        self.create_users_with_farms_locations_and_campaign(email="foo2@bar.com", password="password",
                                                 street="Schmedeswurth 10", zip_code="25724",
                                                 info="Hof Hinrichs", date_from=start, date_to=end, point=Point(9.041581, 53.926445))

        self.create_users_with_farms_locations_and_campaign(email="foo3@bar.com", password="password",
                                                 street="Hauptstraße 25", zip_code="25704",
                                                 info="Ferienhof Boie", date_from=start, date_to=end, point=Point(9.013977, 54.113866))

        self.create_users_with_farms_locations_and_campaign(email="foo4@bar.com", password="password",
                                                 street="Niendieker Strot 47", zip_code="25724",
                                                 info="Gemüsehof Peters", date_from=start, date_to=end, point=Point(9.002436, 53.912535))

        self.create_users_with_farms_locations_and_campaign(email="foo5@bar.com", password="password",
                                                 street="Hochdonner Chaussee 18", zip_code="25712",
                                                 info="Bauernhof Schröfer ", date_from=start, date_to=end, point=Point(9.267870, 54.006127))

        self.create_users_with_farms_locations_and_campaign(email="foo6@bar.com", password="password",
                                                 street="Bahnhofstraße 76", zip_code="25712",
                                                 info="Bauernhof Musfeldt", date_from=start, date_to=end, point=Point(9.255936, 54.003762))

        self.create_users_with_farms_locations_and_campaign(email="foo7@bar.com", password="password",
                                                 street="Fasanenweg 10", zip_code="25584",
                                                 info="Bauernhof Clausen", date_from=start, date_to=end, point=Point(9.310249, 54.035923))

        self.create_users_with_farms_locations_and_campaign(email="foo8@bar.com", password="password",
                                                 street="Bahnhofstraße 29", zip_code="25715",
                                                 info="Bauernhof Schatt", date_from=start, date_to=end, point=Point(9.140065, 53.948425))

        self.create_users_with_farms_locations_and_campaign(email="foo9@bar.com", password="password",
                                                 street=" Nordring 12", zip_code="25704",
                                                 info="Bauernhof Meier", date_from=start, date_to=end, point=Point(9.168022, 54.103823))

        self.create_users_with_farms_locations_and_campaign(email="foo10@bar.com", password="password",
                                                 street="Lehmberg 1", zip_code="25725",
                                                 info="Ferienhof Bothmann", date_from=start, date_to=end, point=Point(9.301864, 54.051955))

        self.create_users_with_farms_locations_and_campaign(email="foo11@bar.com", password="password",
                                                            street="Oberrieder Straße 10", zip_code="86488",
                                                            info="Ferienhof Lecheler GbR - Hofladen", date_from=start, date_to=end,
                                                            point=Point(10.291094, 48.234387))

        self.create_users_with_farms_locations_and_campaign(email="foo12@bar.com", password="password",
                                                            street="Haslacherweg 4-5", zip_code="86498",
                                                            info="Ferien- und Kräuterlandhof Spaun", date_from=start,
                                                            date_to=end,
                                                            point=Point(10.287007, 48.209252))

        self.create_users_with_farms_locations_and_campaign(email="foo13@bar.com", password="password",
                                                            street="Schulstraße 15", zip_code="89233 Neu-Ulm",
                                                            info="Bauernhof Frank", date_from=start,
                                                            date_to=end,
                                                            point=Point(10.041294, 48.408317))

        self.create_users_with_farms_locations_and_campaign(email="foo14@bar.com", password="password",
                                                            street="Münsterweg 9", zip_code="89233 Neu-Ulm",
                                                            info="Traub Hofladen", date_from=start,
                                                            date_to=end,
                                                            point=Point(10.033944, 48.343921))

        self.create_users_with_farms_locations_and_campaign(email="foo15@bar.com", password="password",
                                                            street="Neu-Ulmer Str. 5", zip_code="89233 Neu-Ulm",
                                                            info="Michlabauer", date_from=start,
                                                            date_to=end,
                                                            point=Point(10.069806, 48.362199))

        self.create_users_with_farms_locations_and_campaign(email="foo16@bar.com", password="password",
                                                            street="Münchner Straße 23", zip_code="85604 Zorneding",
                                                            info="Bauernmarkt Zorneding", date_from=start,
                                                            date_to=end,
                                                            point=Point(11.818700, 48.083018))

        self.create_users_with_farms_locations_and_campaign(email="foo17@bar.com", password="password",
                                                            street="Feldmochinger Straße 400", zip_code="80995 München",
                                                            info="Zehentmeier-Hof", date_from=start,
                                                            date_to=end,
                                                            point=Point(11.529329, 48.216521))

        self.create_users_with_farms_locations_and_campaign(email="foo18@bar.com", password="password",
                                                            street="Am Wegfeld 21", zip_code="90427 Nürnberg",
                                                            info="Link Gemüse Hofladen", date_from=start,
                                                            date_to=end,
                                                            point=Point(11.048437, 49.492350))

    def create_users_with_farms_locations_and_campaign(self, email, password, street, zip_code, info, date_from,
                                                       date_to, point, location_type=1):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create_user(email=email, password=password)
            farm = Farm.objects.create(street=street, zip_code=zip_code, user_id=user, point=point)
            location = Location.objects.create(info=info, farm_id=farm, location_type=location_type, point=point)
            self.create_campaign(farm=farm, location=location, date_from=date_from, date_to=date_to)

        return user

    @staticmethod
    def create_campaign(farm, location, date_from, date_to):
        campaign = Campaign.objects.create(farm_id=farm, location_id=location, date_from=date_from, date_to=date_to)
        return campaign
