### I used this file just to debug the code and solve problems with a small set of data

from adittional_functions import *

# Defining minimum driving distance between sales_rep and client
min_distance2 = 10800

sales_rep_fixed2 = (
    ["William Lutz", 4, 25, {"lat": 37.126151, "lon": -112.408145}, 0],
    ["Steven Jorgensen", 3, 16, {"lat": 37.126151, "lon": -112.408145}, 1],
    ["Frances Burchett", 5, 24, {"lat": 37.626634, "lon": -109.859781}, 1],
    ["Patrick Young", 5, 18, {"lat": 39.500985, "lon": -112.268499}, 0],
    ["Renaldo Hennon", 3, 15, {"lat": 39.399315, "lon": -109.328555}, 1],
)

clients_fixed2 = (
    [0, {"lat": 37.626634, "lon": -109.859784}],
    [1, {"lat": 37.626634, "lon": -109.859785}],
    [2, {"lat": 37.626634, "lon": -109.859786}],
    [3, {"lat": 37.626634, "lon": -109.859787}],
    [4, {"lat": 37.626634, "lon": -109.859788}],
)

"""for rep in sales_rep_fixed:
    for client in clients_fixed:
        dst = driving_time(
            rep[3]["lat"],
            rep[3]["lon"],
            client[1]["lat"],
            client[1]["lon"],
        )
        if dst <= min_distance:
            print("Possible")"""
