### In this file I am generating random data of clients and sales rep
### The data is registered in the file "last_data_used.txt" to be consulted if needed
### The Data is deleted and overwrited each time this file runs

from pickle import FALSE
from socket import AF_X25
import names
import random
from shapely.geometry import Polygon
from adittional_functions import *
import matplotlib.pyplot as plt
import matplotlib.image as img


def generate_data(nr_reps, nr_clients, area):
    """Function that generates the data to be used on the problem
    Data is randomly generated with the following format
    Sales Rep data : ['name', review, experience, {'lat': latitude, 'lon':longitude}, Full/Part time]
    Clients Data : [number id, {'lat': latitude, 'lon':longitude}]


    Args:
        nr_reps (int): number of sales representatives to be generated
        nr_clients (int): number of clients to be generated
        area (Polygon): _description_

    Returns:
        (list, list): lists of lists with sales reps and clients data
    """
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
    for rep in range(nr_reps):
        sales_reps[rep].append(coordinate_generator(area, rep))

    # Defining if the employee is working part-time or full-time will affect the maximum number of clients he/she can be assigned to
    for rep in sales_reps:
        rep.append(random.randint(0, 1))  # 0 == Full-time ; 1 == Part-time

    # Defining clients random locations
    clients = []
    for client in range(nr_clients):
        clients.append([client, coordinate_generator(area, client)])

    # Creating a .txt document to register the data generated
    last_data_used = open("last_data_used.txt", "w")
    last_data_used.write("List of all Sales Representatives : \n \n")
    for rep in sales_reps:
        last_data_used.write(f"{rep},\n")
    last_data_used.write("\n List of all Clients : \n \n")
    for client in clients:
        last_data_used.write(f"{client},\n")
    last_data_used.close()

    return (sales_reps, clients)


def visualize_data(sales_rep, clients, area):
    """This function aimes to show the map of the business area with the clients and sales team locations marked

    Args:
        sales_rep (list): List of sales rep data
        clients (list): list of clients data
        area (Polygon): business area
    """
    # Extract the point values that define the perimeter of the polygon
    area_latitude, area_longitude = area.exterior.coords.xy

    # Define a bounding box
    bbox = (
        min(area_longitude),
        max(area_longitude),
        min(area_latitude),
        max(area_latitude),
    )

    # Defining clients and reps coordintes
    clients_lat = list()
    clients_lon = list()
    ids = list()
    sales_lat = list()
    sales_lon = list()
    names = list()
    for rep in sales_rep:
        names.append(rep[0])
        sales_lat.append(rep[3]["lat"])
        sales_lon.append(rep[3]["lon"])
    for client in clients:
        ids.append(client[0])
        clients_lat.append(client[1]["lat"])
        clients_lon.append(client[1]["lon"])

    img = plt.imread("south_carolina.png")

    fig, ax = plt.subplots(figsize=(12, 10))

    ax.imshow(img, extent=(bbox[0], bbox[1], bbox[2], bbox[3]))

    ax.scatter(clients_lon, clients_lat, c="g", marker="X", s=50)
    ax.scatter(sales_lon, sales_lat, c="b", marker="o", alpha=0.6)

    # Labeling clients and reps on the map
    for i, txt in enumerate(ids):
        ax.annotate(txt, (clients_lon[i], clients_lat[i]))

    for i, txt in enumerate(names):
        ax.annotate(txt, (sales_lon[i], sales_lat[i]))

    plt.title("Sales Reps and Clients locations")
    plt.xlim(bbox[0], bbox[1])
    plt.ylim(bbox[2], bbox[3])
    plt.show()


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

south_carolina = Polygon(
    [
        (32.113859, -80.959657),
        (34.743249, -83.081187),
        (34.999217, -81.162450),
        (33.866511, -78.697035),
    ]
)
