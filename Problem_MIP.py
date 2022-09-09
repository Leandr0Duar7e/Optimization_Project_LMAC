from turtle import distance
from ortools.linear_solver import pywraplp
from Data import *
from adittional_functions import *

# from fixed_vars import *
import copy
import time


def solve_problem(sales_rep_fixed, clients_fixed, min_driving_dst):
    # Data
    # sales_rep = ('name', review, experience, {'lat': latitude, 'lon'= longitude})
    # clients = (number, {'lat': latitude, 'lon'= longitude})

    # Using a fixed set of data to develop the model. See the data on fixed_vars file
    sales_rep = copy.deepcopy(sales_rep_fixed)
    clients = copy.deepcopy(clients_fixed)

    nbr_sales_rep = len(sales_rep)
    nbr_clients = len(clients)

    # Solving
    # Create the MIP solver with the SCIP backend
    solver = pywraplp.Solver.CreateSolver("SCIP")

    # Defining variables
    # x[i,j] is an array of 0-1 variables, which will be 1 if sales rep i is assigned to client j
    x = {}
    for rep in range(nbr_sales_rep):
        for client in range(nbr_clients):
            x[rep, client] = solver.IntVar(0, 1, "")

    # Treating data problems
    # Checking if there's any client with no sales_rep within 3 hours driving and assigning it to the closest one
    for client in range(nbr_clients):
        i = 0
        j = 0  # indice of the closest sales rep
        distance = min_driving_dst + 1
        closest_rep = 10000000  # A never possible driving distance in seconds
        while distance > min_driving_dst and i < nbr_sales_rep:
            distance = driving_time(
                sales_rep[i][3]["lat"],
                sales_rep[i][3]["lon"],
                clients[client][1]["lat"],
                clients[client][1]["lon"],
            )
            if (
                distance < closest_rep
            ):  # ignoring the possibility of two different sales_rep at the same driving distance from this client
                closest_rep = distance
                j = i
            i += 1
        if (
            i == nbr_sales_rep and closest_rep > min_driving_dst
        ):  # Both conditions to prevent the case that the last rep on the list is within the minimum driving time
            solver.Add(
                x[j, client] == 1
            )  # making mandatory that this client is associated with the closest rep
            clients[client][1]["lat"] = sales_rep[j][3][
                "lat"
            ]  # Reduce the distance so it does not cause problems in the driving time constraint
            clients[client][1]["lon"] = sales_rep[j][3]["lon"]
            print("!Too Far!")
        else:
            print("Sales Rep found")

    # Constraints
    # Each client is assigned to exactly one sales rep
    for client in range(nbr_clients):
        solver.Add(solver.Sum([x[rep, client] for rep in range(nbr_sales_rep)]) == 1)

    # Each client must be at most at 3 hours (10800 s) driving from its sales rep (choose the closest if there's none in those conditions)
    for rep in range(nbr_sales_rep):
        for client in range(nbr_clients):
            driving_dst = driving_time(
                sales_rep[rep][3]["lat"],
                sales_rep[rep][3]["lon"],
                clients[client][1]["lat"],
                clients[client][1]["lon"],
            )
            solver.Add(driving_dst * x[rep, client] <= min_driving_dst)

    # Each sales_rep working full_time can have at most 8 clients assigned and part_time can have at most 4
    for rep in range(nbr_sales_rep):
        solver.Add(
            solver.Sum([x[rep, client] for client in range(nbr_clients)])
            <= (8 - 4 * sales_rep[rep][4])
        )

    # Objective
    objective_terms = []
    for rep in range(nbr_sales_rep):
        for client in range(nbr_clients):
            objective_terms.append(
                x[rep, client]
                * (
                    1
                    - (0.75 * (sales_rep[rep][1] / 5) + 0.25 * (sales_rep[rep][2] / 25))
                )  # Establishing the differentiator factors between  sales_rep being those reviews and experience with different levels of impact
            )
    solver.Minimize(solver.Sum(objective_terms))

    # Print Solution

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        for client in range(nbr_clients):
            for rep in range(nbr_sales_rep):
                # Testing if x[i,j] is 1(with tolerance for floating point arithmetic)
                if x[rep, client].solution_value() > 0.5:
                    dst = driving_time(
                        sales_rep_fixed[rep][3]["lat"],
                        sales_rep_fixed[rep][3]["lon"],
                        clients_fixed[client][1]["lat"],
                        clients_fixed[client][1]["lon"],
                    )
                    hours = round(dst // 3600)
                    minutes = round((dst % 3600) // 60)
                    seconds = round(((dst % 3600) % 60) * 60)
                    print(
                        f"Sales rep {sales_rep[rep][0]} assigned to client {clients[client][0]}."
                        + f"\n Driving distance: {hours}h {minutes}m {seconds}s \n"
                    )
        return True
    else:
        print("No solution found.")
        return False
