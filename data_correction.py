### If the model founds no solution there's 2 problems I am solving here concerning the data
###
### 1: There's no sales rep within the minimum driving distance of a client
### Solution : Assign the closest rep to this client
###
### 2: There's x clients that are only within the driving time of sales rep A and the number x exceeds the
### maximum of clients that sales rep can support
### Solution : Assign the furthest client to its second closest sales rep

from adittional_functions import *


def data_correction_1(sales_data, clients_data, driving_data):
    pairs_list = list()  # list of the indices of clients and sales rep to be associated
    # Checking if there's any client with no sales_rep within 3 hours driving and assigning it to the closest one
    nr_sales = len(sales_data)
    nr_clients = len(clients_data)
    for client in range(nr_clients):
        i = 0
        j = 0  # indice of the closest sales rep
        distance = driving_data + 1
        closest_rep = 10000000  # A never possible driving distance in seconds
        while distance > driving_data and i < nr_sales:
            distance = driving_time(
                sales_data[i][3]["lat"],
                sales_data[i][3]["lon"],
                clients_data[client][1]["lat"],
                clients_data[client][1]["lon"],
            )
            if (
                distance < closest_rep
            ):  # ignoring the possibility of two different sales_rep at the same driving distance from this client
                closest_rep = distance
                j = i
            i += 1
        if (
            i == nr_sales and closest_rep > driving_data
        ):  # Both conditions to prevent the case that the last rep on the list is within the minimum driving time
            pairs_list.append([j, client])
            print("An error was solved!")
    return pairs_list
