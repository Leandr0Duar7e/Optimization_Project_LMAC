### This file was used to fix a set of data and optimize the model, debug and solve appearing problems

from Data import *
from adittional_functions import *

sales_rep_fixed2 = [
    ["Patricia Antczak", 2, 16, {"lat": 33.841876, "lon": -80.651853}, 0],
    ["Carol Byrne", 2, 21, {"lat": 33.896459, "lon": -82.151267}, 0],
    ["Linda Miller", 1, 21, {"lat": 33.306674, "lon": -80.763327}, 1],
    ["Audra Landrum", 2, 19, {"lat": 33.32207, "lon": -80.734774}, 0],
    ["Antoinette Enama", 5, 3, {"lat": 34.443404, "lon": -80.005495}, 0],
    ["Devon Rolan", 4, 2, {"lat": 34.12193, "lon": -81.734821}, 0],
    ["Tonisha Staton", 1, 9, {"lat": 32.834586, "lon": -80.524548}, 1],
    ["Rupert Mcclenon", 4, 12, {"lat": 33.551343, "lon": -81.204525}, 1],
    ["Dustin Pace", 3, 18, {"lat": 33.670143, "lon": -80.44195}, 1],
    ["Jeffrey Watson", 1, 16, {"lat": 34.252533, "lon": -81.498841}, 1],
]

clients_fixed2 = [
    [0, {"lat": 34.387118, "lon": -80.35856}],
    [1, {"lat": 34.311828, "lon": -81.032079}],
    [2, {"lat": 33.227809, "lon": -81.60056}],
    [3, {"lat": 32.705011, "lon": -80.323957}],
    [4, {"lat": 34.170822, "lon": -81.396378}],
    [5, {"lat": 34.561999, "lon": -82.046815}],
    [6, {"lat": 32.804847, "lon": -81.110171}],
    [7, {"lat": 33.319785, "lon": -81.405759}],
    [8, {"lat": 34.388909, "lon": -79.938952}],
    [9, {"lat": 34.677759, "lon": -81.849256}],
    [10, {"lat": 33.013027, "lon": -80.220606}],
    [11, {"lat": 32.942335, "lon": -80.927234}],
    [12, {"lat": 34.844368, "lon": -81.164566}],
    [13, {"lat": 34.542162, "lon": -80.271372}],
    [14, {"lat": 33.283961, "lon": -81.643797}],
    [15, {"lat": 33.094594, "lon": -80.409542}],
    [16, {"lat": 34.173572, "lon": -79.921626}],
    [17, {"lat": 34.541488, "lon": -81.457591}],
    [18, {"lat": 32.450507, "lon": -80.666583}],
    [19, {"lat": 32.703842, "lon": -80.681873}],
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
