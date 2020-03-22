from rest_framework import viewsets
from rest_framework import permissions
from rest_server.models import Farm, User, Campaign, Location
from rest_framework.generics import RetrieveUpdateAPIView
from rest_server.serializers import (UserSerializer, FarmSerializer, LocationSerializer, RegistrationSerializer,
                                     LoginSerializer, UserSerializer, CampaignSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_server.renderers import UserJSONRenderer
from rest_framework.decorators import action
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.core.serializers import serialize as djangoSerializer
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class FarmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = []


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        response['JWT'] = serializer.data['token']
        return response


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['JWT'] = serializer.data['token']
        return response


def get_radius_point_from_request(request):
    radius = request.query_params.get('radius', None)
    lat = request.query_params.get('lat', None)
    lng = request.query_params.get('lng', None)
    point = Point(float(lng), float(lat))

    return radius, point


class CampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campaigns to be viewed or edited and searched.
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = []

    @action(detail=False)
    def find_in_radius(self, request):
        try:
            radius, point = get_radius_point_from_request(request)
        except:
            return Response('missing required parameter, radius, lat or lng is invalid',
                            status=status.HTTP_400_BAD_REQUEST)

        filtered_campaigns = Campaign.objects.filter(location_id__point__distance_lt=(point, Distance(km=radius)))
        serializer = self.get_serializer(filtered_campaigns, many=True)
        return Response(serializer.data)


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows locations to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = []

    @action(detail=False)
    def all_as_geo_json(self, request):
        data = djangoSerializer('custom_geojson', Location.objects.all(),
                                geometry_field='point',
                                fields=('id', 'point', 'info', 'farm_id', 'location_type'))

        return Response(json.loads(data))

    @action(detail=False)
    def find_in_radius_as_geo_json(self, request):
        try:
            radius, point = get_radius_point_from_request(request)
        except:
            return Response('missing required parameter, radius, lat or lng is invalid',
                            status=status.HTTP_400_BAD_REQUEST)

        filtered_locations = Location.objects.filter(point__distance_lt=(point, Distance(km=radius)))
        data = djangoSerializer('custom_geojson', filtered_locations,
                                geometry_field='point',
                                fields=('id', 'point', 'info', 'farm_id', 'location_type'))
        return Response(data)
