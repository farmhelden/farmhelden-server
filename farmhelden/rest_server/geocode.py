import googlemaps

def get_coordinates(query):
    gmaps = googlemaps.Client(key='')
    response = gmaps.geocode(query)
    lat = response[0]['geometry']['location']['lat']
    lng = response[0]['geometry']['location']['lng']

    return lat,lng
