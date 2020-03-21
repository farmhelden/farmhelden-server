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

class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'password', 'token']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)