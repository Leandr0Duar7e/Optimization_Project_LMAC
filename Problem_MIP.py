from ortools.linear_solver import pywraplp
from Data import *
from adittional_functions import *


def main():
    # Defining the Data
    # sales_rep = ('name', review, experience, {'lat': latitude, 'lon'= longitude})
    # clients = (number, {'lat': latitude, 'lon'= longitude})
    sales_rep, clients = generate_data()

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

    # Each client must be at most at 3 hours (108000 s) driving from its sales rep (choose the closest if there's none in those conditions)
    for rep in range(nbr_sales_rep):
        for client in range(nbr_clients):
            solver.Add(
                driving_time(
                    sales_rep[rep][3]["lon"],
                    sales_rep[rep][3]["lat"],
                    clients[client][1]["lon"],
                    clients[client][1]["lat"],
                )
                * x[rep, client]
                <= 10800
            )

    # Objective
    objective_terms = []
    for rep in range(nbr_sales_rep):
        for client in range(nbr_clients):
            objective_terms.append(x[rep, client])
    solver.Minimize(solver.Sum(objective_terms))


if __name__ == "__main__":
    main()
