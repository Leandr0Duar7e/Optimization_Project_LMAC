### In this file I am generating random data of clients and sales rep
### The data is registered in the file "last_data_used.txt" to be consulted if needed
### The Data is deleted and overwrited each time this file runs

from socket import AF_X25
import names
import random
from shapely.geometry import Polygon
from adittional_functions import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as img


def generate_data(nr_reps, nr_clients, area):
    # Sales Rep data : ['name', review, experience, {'lat': latitude, 'lon':longitude}, Full/Part time]
    # Defining random sales rep names
    sales_names = []
    for i in range(nr_reps):
        sales_names.append(names.get_full_name())

    # Defining random sales rep average reviews between 1 and 5
    sales_reps = []
    for rep in sales_names:
        sales_reps.append(
            [rep, random.randint(1, 5)]
        )  # We assume every sales rep has reviews and zero is not an option

    # Defining random sales rep years of experience between 0 and 25
    for rep in sales_reps:
        rep.append(
            random.randint(0, 25)
        )  # zero corresponds to less than an year of experience and 25 is the maximum

    # Defining random sales rep location
    for rep in sales_reps:
        rep.append(coordinate_generator(area))

    # Adding reps locations in usa2 area
    # Defining if the employee is working part-time or full-time will affect the maximum number of clients he/she can be assigned to
    for rep in sales_reps:
        rep.append(random.randint(0, 1))  # 0 == Full-time ; 1 == Part-time

    # Defining clients random locations
    # Clients are defined by (number, location)
    clients = []
    for client in range(nr_clients):
        clients.append([client, coordinate_generator(area)])

    last_data_used = open("last_data_used.txt", "w")
    last_data_used.write("List of all Sales Representatives : \n \n")
    for rep in sales_reps:
        last_data_used.write(f"{rep} \n")
    last_data_used.write("\n List of all Clients : \n \n")
    for client in clients:
        last_data_used.write(f"{client} \n")
    # last_data_used.write(f"{sales_reps} \n {clients}")
    last_data_used.close()

    return (sales_reps, clients)


def visualize_data(sales_rep, clients, area):
    # Extract the point values that define the perimeter of the polygon
    area_latitude, area_longitude = area.exterior.coords.xy

    # Define a bounding box
    bbox = (
        min(area_longitude),
        max(area_longitude),
        min(area_latitude),
        max(area_latitude),
    )

    # state of utah image
    utha = img.imread("utah.png")

    fig, ax = plt.subplots(figsize=(8, 12))

    # Defining clients and reps coordintes
    clients_lat = list()
    clients_lon = list()
    sales_lat = list()
    sales_lon = list()
    for rep in sales_rep:
        sales_lat.append(rep[3]["lat"])
        sales_lon.append(rep[3]["lon"])
    for client in clients:
        clients_lat.append(client[1]["lat"])
        clients_lon.append(client[1]["lon"])

    ax.scatter(sales_lon, sales_lat, zorder=1, alpha=0.2, c="b", s=10)
    ax.scatter(sales_lon, sales_lat, zorder=1, alpha=0.2, c="r", s=10)

    ax.set_title("Plotting Sales Reps and Clients locations")
    ax.set_xlim(bbox[0], bbox[1])
    ax.set_ylim(bbox[2], bbox[3])

    ax.imshow(utah, zorder=0, extent=bbox, aspect="equal")


# Defining different geographical areas
# Defining an area that simulates the USA with points as (latitude, longitude)
usa = Polygon(
    [
        (48, -124),
        (48, -95),
        (41, -83),
        (44, -67),
        (29, -82),
        (29, -98),
        (33, -117),
        (40, -123),
    ]
)

# Defining an area that represents California, Utah, Arizona and Nevada
usa2 = Polygon(
    [
        (41.909652, -124.137352),
        (41.951336, -111.105839),
        (40.939755, -111.114648),
        (40.970688, -109.086878),
        (31.363741, -109.068074),
        (31.374897, -111.067022),
        (32.769783, -114.712162),
        (32.639949, -117.054591),
    ]
)

# Defining the area of Utah
utah = Polygon(
    [
        (41.971607, -113.999901),
        (41.990605, -111.061827),
        (40.994451, -111.051102),
        (41.000347, -109.050359),
        (36.999538, -109.046141),
        (37.005644, -114.040360),
    ]
)

portugal_sul = Polygon(
    [
        (37.958085, -8.884172),
        (37.898001, -8.756783),
        (37.085305, -8.782972),
        (37.168827, -8.375586),
        (37.192011, -7.435687),
        (37.559599, -7.577416),
        (37.937197, -7.307499),
    ]
)
