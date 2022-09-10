### In this file you can define: number of sales representatives;
# Number of clients; The geographical area to work on;
# The minimum driving distance between client and rep.
#
# After defining the model will be run and if there's no solution,
# data will be treated and a solution must arise within two attempts
#
# If there's no solution at the end than the Data given does not make sense

import time
from Problem_MIP import *
from Data import *
from data_correction import *

# from fixed_vars import *

start_time = time.time()

# Define number of reps and clients
nr_sales_rep = 40
nr_clients = 70

# Define the minimum driving distance in seconds
min_drive_dst = 10800

# Generating Data
sales, clients = generate_data(nr_sales_rep, nr_clients, utah)
# sales, clients = sales_rep_fixed2, clients_fixed2

# Solving the problem
if nr_clients <= 0 or nr_sales_rep <= 0 or min_drive_dst <= 0:
    print("Data does not make sense")
    exit()

indices = list()
if solve_problem(sales, clients, min_drive_dst, indices) == False:
    print("Treating Data ...")
    indices += data_correction_1(sales, clients, min_drive_dst)
    print("Done! Let's try to solve this problem again...")
    if solve_problem(sales, clients, min_drive_dst, indices) == False:
        print("Treating Data ... \n This one might take a while!")
        indices += data_correction_2(sales, clients, min_drive_dst)
        print("Done! Let's try to solve this problem again...")
        # print(indices)
        if solve_problem(sales, clients, min_drive_dst, indices) == False:
            print("The problem is impossible to solve! \n Please review the data.")


# Printing execution time
print("--- --- --- \n Execution time = %s seconds " % round((time.time() - start_time)))
