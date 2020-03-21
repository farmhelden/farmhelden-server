from rest_framework import serializers
from rest_server.models import Farm, User
from rest_server.geocode import get_coordinates
from django.contrib.gis.geos import Point

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class FarmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farm
        fields = ['id', 'zip_code', 'street', 'point']

    def create(self, validated_data):
        object =  Farm.objects.create(**validated_data)
        try:
            lat, lng = get_coordinates("address " + object.zip_code + " " + object.street)
            object.point = Point(lat, lng)
            object.save()
        except:
            print('error while geocoding, did you set a google api key?')

        return object
