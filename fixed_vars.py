### I used this file just to debug the code and solve problems with a small set of data
from Data import *
from adittional_functions import *

# Defining minimum driving distance between sales_rep and client
min_distance2 = 10800

sales_rep_fixed2 = [
    ["Mary Brewer", 1, 6, {"lat": 39.861418, "lon": -111.848897}, 0],
    ["Ashley Dunbar", 1, 8, {"lat": 38.681954, "lon": -113.015716}, 0],
    ["Kaitlin Ferrusi", 5, 18, {"lat": 40.907344, "lon": -112.822572}, 0],
    ["Betty Brooks", 3, 24, {"lat": 38.493502, "lon": -112.227556}, 1],
    ["Erica Jones", 2, 6, {"lat": 41.307044, "lon": -112.88527}, 1],
    ["Donnie Kinloch", 4, 15, {"lat": 38.039264, "lon": -109.341645}, 0],
    ["Nicole Richardson", 5, 6, {"lat": 39.278208, "lon": -110.181014}, 0],
]

clients_fixed2 = [
    [0, {"lat": 41.760381, "lon": -112.170096}],
    [1, {"lat": 38.476642, "lon": -113.67096}],
    [2, {"lat": 40.417933, "lon": -113.295405}],
    [3, {"lat": 38.10251, "lon": -109.198764}],
    [4, {"lat": 39.965339, "lon": -109.82835}],
]

# visualize_data(sales_rep_fixed2, clients_fixed2, utah)
