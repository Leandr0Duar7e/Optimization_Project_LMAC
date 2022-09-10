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
nr_sales_rep = 10
nr_clients = 5

# Define the minimum driving distance in seconds
min_drive_dst = 10800

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
