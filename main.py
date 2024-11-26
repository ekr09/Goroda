from opencage.geocoder import OpenCageGeocode


def get_coordinates(city,key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return 'Город не найден'


key = '49f2646c23fe46299695b0573c0b5080'
city ='Moscow'
coordinates = get_coordinates(city, key)
print (f'Координаты города {city}: {coordinates}')