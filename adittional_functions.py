import requests
import json

# Calling the OpenStreetMap API and using json library to get the response
def driving_time(lon_1, lat_1, lon_2, lat_2):
    r = requests.get(
        f"""http://router.project-osrm.org/route/v1/car/{lat_1},{lon_1};{lat_2},{lon_2}?overview=false"""
    )
    print("a")
    print(r.content)
    routes = json.loads(r.content)["routes"][0]

    return routes["duration"]


print(driving_time(38.808809, -111.339107, 39.196708, -112.081877))
