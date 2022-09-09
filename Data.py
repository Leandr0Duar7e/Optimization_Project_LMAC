import numpy as np
import names
import random
from shapely.geometry import Polygon
from adittional_functions import *

# Here I want to include all data needed for the project
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
        rep.append(coordinate_generator(area))  # Adding reps locations in usa2 area

    # Defining if the employee is working part-time or full-time will affect the maximum number of clients he/she can be assigned to
    for rep in sales_reps:
        rep.append(random.randint(0, 1))  # 0 == Full ; 1 == Part

    # Defining clients random locations
    # Clients are defined by (number, location)
    clients = []
    for client in range(nr_clients):
        clients.append([client, coordinate_generator(area)])

    return (sales_reps, clients)
