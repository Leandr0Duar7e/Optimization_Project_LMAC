### This file was used to fix a set of data and optimize the model, debug and solve appearing problems

from Data import *
from adittional_functions import *

sales_rep_fixed2 = [
    ["Randall Larkin", 2, 16, {"lat": 34.401102, "lon": -80.442628}, 1],
    ["George Powell", 3, 12, {"lat": 34.104101, "lon": -80.924947}, 1],
    ["Kristina Genet", 4, 9, {"lat": 33.245303, "lon": -81.378793}, 0],
    ["Jessica Brooks", 2, 2, {"lat": 33.487323, "lon": -80.236988}, 1],
    ["John Vasquez", 3, 15, {"lat": 33.852873, "lon": -80.514586}, 0],
    ["Evelyn Hernandez", 1, 13, {"lat": 34.213974, "lon": -79.768324}, 0],
    ["Vera Miller", 2, 17, {"lat": 33.000601, "lon": -80.993143}, 0],
]

clients_fixed2 = [
    [0, {"lat": 33.897938, "lon": -79.418141}],
    [1, {"lat": 34.592222, "lon": -82.968292}],
    [2, {"lat": 32.558635, "lon": -80.703884}],
    [3, {"lat": 33.49271, "lon": -80.326073}],
    [4, {"lat": 33.955242, "lon": -80.280544}],
    [5, {"lat": 34.342664, "lon": -82.040896}],
    [6, {"lat": 33.043448, "lon": -80.645763}],
    [7, {"lat": 33.366307, "lon": -81.197821}],
    [8, {"lat": 34.068536, "lon": -79.540536}],
    [9, {"lat": 33.856141, "lon": -80.917737}],
    [10, {"lat": 32.943726, "lon": -80.53213}],
    [11, {"lat": 33.26562, "lon": -81.540869}],
    [12, {"lat": 33.667415, "lon": -80.823989}],
    [13, {"lat": 33.707715, "lon": -81.275005}],
    [14, {"lat": 33.476923, "lon": -81.385967}],
    [15, {"lat": 32.557737, "lon": -80.856303}],
    [16, {"lat": 34.290586, "lon": -81.291135}],
    [17, {"lat": 33.745449, "lon": -80.256602}],
    [18, {"lat": 32.68058, "lon": -80.936057}],
    [19, {"lat": 33.137256, "lon": -81.036352}],
]

# visualize_data(sales_rep_fixed2, clients_fixed2, south_carolina)
# for rep in sales_rep_fixed2:
# print(
# driving_time(
# rep[3]["lat"],
# rep[3]["lon"],
# clients_fixed2[1][1]["lat"],
# clients_fixed2[1][1]["lon"],
# )
# )
