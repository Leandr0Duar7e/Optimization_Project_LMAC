from ortools.linear_solver import pywraplp
from Data import *
from adittional_functions import *
from configparser import ConfigParser
import os

# from fixed_vars import *
import copy


def solve_problem(sales_rep_fixed, clients_fixed, max_driving_dst, index):
    """MIP Solver optimizing the number of sales reps needed to address all clients
    Given variables, constraints and an objective function the solver returns
    the associations between clients and reps

    Args:
        sales_rep_fixed (list): list of sales reps
        clients_fixed (list): list of clients
        max_driving_dst (int): maximum driving time in seconds
        index (list): list of clients to be removed from data

    Returns:
        dict: matrix of boolean variables indicating if a client is associated with a sales rep
    """
    # Data
    # sales_rep = ('name', review, experience, {'lat': latitude, 'lon'= longitude})
    # clients = (number, {'lat': latitude, 'lon'= longitude})

    CONFIG_PATH = os.getcwd() + r"/config.ini"

    config = ConfigParser()
    config.read(CONFIG_PATH)

    # Using a fixed set of data to develop the model. See the data on fixed_vars file
    sales_rep = copy.deepcopy(
        sales_rep_fixed
    )  # deepcopy to maintain the driving distance data that can be changed to zero in problematic cases
    clients = copy.deepcopy(clients_fixed)

    # Treating Data
    # Check if there is any client to be removed
    if index != []:
        update = 0
        for i in index:
            clients.pop(i - update)
            update += 1

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
            solver.Add(driving_dst * x[rep, client] <= max_driving_dst)

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
                    - (
                        float(config.get("OPTIMIZER", "AVERAGE_REVIEW_WEIGHT"))
                        * (sales_rep[rep][1] / 5)
                        + float(config.get("OPTIMIZER", "EXPERIENCE_WEIGHT"))
                        * (sales_rep[rep][2] / 25)
                    )
                )  # Establishing the differentiator factors between  sales_rep being those reviews and experience with different levels of impact
            )
    solver.Minimize(solver.Sum(objective_terms))

    # Print Solution

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        working_reps = 0
        reps_needed = list()
        for rep in range(nbr_sales_rep):
            show = 0
            for client in range(nbr_clients):
                # Testing if x[i,j] is 1(with tolerance for floating point arithmetic)
                if x[rep, client].solution_value() > 0.5:
                    reps_needed.append(sales_rep[rep])
                    dst = driving_time(
                        sales_rep[rep][3]["lat"],
                        sales_rep[rep][3]["lon"],
                        clients[client][1]["lat"],
                        clients[client][1]["lon"],
                    )
                    hours = round(dst // 3600)
                    minutes = round((dst % 3600) // 60)
                    seconds = round((dst % 3600) % 60)
                    if show < 1:
                        print(
                            f"\nSales rep: {sales_rep[rep][0]}   ||  Average review: {sales_rep[rep][1]}   ||  Years of Experience: {sales_rep[rep][2]}  || Working",
                            end="",
                        )
                        if sales_rep[rep][4] == 0:
                            print(" full time.")
                        else:
                            print(" part time.")
                        print(f"List of clients assigned to {sales_rep[rep][0]}:\n")
                    print(
                        f"Client {clients[client][0]} -> Driving distance: {hours}h {minutes}m {seconds}s"
                    )
                    show += 1
            if show > 0:
                working_reps += 1
        print(
            f"\nWorkforce optimization from {nbr_sales_rep} to {working_reps} sales representatives."
        )
        visualize_data(reps_needed, clients, south_carolina)

        return x
    else:
        print("No solution found.")
        return False
