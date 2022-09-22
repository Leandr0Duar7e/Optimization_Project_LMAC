### This is the main file were other files' functions are called
### Data will be generated, treated if necessary and the a solution will arise from our model's solver

import time
from Problem_MIP import *
from Data import *
from data_correction import *
from configparser import ConfigParser
import os

# from fixed_vars import *

start_time = time.time()

# Getting the number of reps and clients and the minimum driving distanve from config.ini file
CONFIG_PATH = os.getcwd() + r"/config.ini"

config = ConfigParser()
config.read(CONFIG_PATH)

nr_sales_rep = int(config.get("DATA_CONFIG", "NR_SALES_REPS"))
nr_clients = int(config.get("DATA_CONFIG", "NR_CLIENTS"))

min_drive_dst = int(config.get("DATA_CONFIG", "MAX_DRIVING_DISTANCE"))

# Generating Data
sales, clients = generate_data(nr_sales_rep, nr_clients, south_carolina)
# sales, clients = (sales_rep_fixed2, clients_fixed2)

# Checking if logical requirements are met
if nr_clients <= 0 or nr_sales_rep <= 0 or min_drive_dst <= 0:
    print("Data does not make sense")
    exit()

# Plotting the data
visualize_data(sales, clients, south_carolina)

indices = (
    list()
)  # This list will contain the clients numbers that are impossible to reach with the companys' workforce
if (
    solve_problem(sales, clients, min_drive_dst, indices) == False
):  # False means no solution was found
    print("Treating Data ...")
    indices += data_correction_1(sales, clients, min_drive_dst)
    print("Done! Let's try to solve this problem again...")
    if solve_problem(sales, clients, min_drive_dst, indices) == False:
        print("Treating Data ... \n   This one might take a while!")
        indices += data_correction_2(sales, clients, min_drive_dst)
        print("Done! Let's try to solve this problem again...")
        if solve_problem(sales, clients, min_drive_dst, indices) == False:
            print("The problem is impossible to solve! \n Please review the data.")


# Printing execution time
print("--- --- --- \n Execution time = %s seconds " % round((time.time() - start_time)))
