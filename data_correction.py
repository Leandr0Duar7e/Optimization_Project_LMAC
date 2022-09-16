### If the model founds no solution there's 2 problems I am solving here concerning the data
###
### 1: There's no sales rep within the maximum driving distance of a client
### Solution : Remove the client from data
###
### 2: There's x clients that are only within the driving time of sales rep A and the number x exceeds the
### maximum of clients that sales rep can support
### Solution : Remove the furthest clients until the limit is not exceeded

from adittional_functions import *


def data_correction_1(sales_data, clients_data, driving_data):
    """Checks for clients with no sales reps within the maximum driving distance and removes them from the data set

    Args:
        sales_data (list): list of sales reps
        clients_data (list): list of clients
        driving_data (int): maximum driving time in seconds

    Returns:
        list: list of clients to be removed from data
    """
    remove_list = list()  # list of the indices of clients to be removed from data sets
    nr_sales = len(sales_data)
    nr_clients = len(clients_data)
    for client in range(nr_clients):
        i = 0
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
            i += 1
        if (
            i == nr_sales and closest_rep > driving_data
        ):  # Both conditions to prevent the case that the last rep on the list is within the minimum driving time
            remove_list.append(client)
            print(
                f"An error was solved!\nClient {client} location is too far to be adressed."
            )
    return remove_list


def data_correction_2(sales_data, clients_data, driving_data):
    """Checks for clients that have only one sales rep within the maximum driving distance but that
    sales rep has already exceeded its maximum capacity of clients adressed
    It will remove from data the furthest client from this sales rep

    Args:
        sales_data (list): list of sales
        clients_data (list): list of clients
        driving_data (int): maximum driving time in seconds

    Returns:
        list: list of clients to be removed from data
    """
    remove_list = list()
    nr_sales = len(sales_data)
    nr_clients = len(clients_data)
    reps_list = [
        [] for _ in range(nr_sales)
    ]  # list containing, for each sales rep, the clients that are only within the minimum driving distance from them

    for client in range(nr_clients):
        options = 0
        i = 0
        rep = 0
        while options < 2 and i < nr_sales:
            distance = driving_time(
                sales_data[i][3]["lat"],
                sales_data[i][3]["lon"],
                clients_data[client][1]["lat"],
                clients_data[client][1]["lon"],
            )
            if distance <= driving_data:
                options += 1
                rep = i
            i += 1
        if (
            options == 1
        ):  # It checks the clients that have only one rep option witin the minimum driving time
            reps_list[rep].append(client)

    for rep in range(nr_sales):
        nr = len(reps_list[rep])
        while nr > (
            8 - sales_data[rep][4] * 4
        ):  # Checks if the sales rep have more clients adressed than he can handle
            furthest = 0
            for client in range(nr - 1):
                dst1 = driving_time(
                    sales_data[rep][3]["lat"],
                    sales_data[rep][3]["lon"],
                    clients_data[reps_list[rep][furthest]][1]["lat"],
                    clients_data[reps_list[rep][furthest]][1]["lon"],
                )
                dst2 = driving_time(
                    sales_data[rep][3]["lat"],
                    sales_data[rep][3]["lon"],
                    clients_data[reps_list[rep][client + 1]][1]["lat"],
                    clients_data[reps_list[rep][client + 1]][1]["lon"],
                )
                if dst2 > dst1:
                    furthest = client + 1  # keeps the indice of the furthest client
            nr -= 1
            print(
                f"An error was solved!\nClient {reps_list[rep][furthest]} location is too far to be adressed."
            )
            remove_list.append(reps_list[rep].pop(furthest))
    return remove_list
