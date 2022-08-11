import numpy as np
import names
import random
from shapely.geometry import Polygon, Point

# Here I want to include all data needed for the project
def generate_data():
    # Sales Rep data : ['name', review, experience, {'lat': latitude, 'lon':longitude}, salary]
    # Defining random sales rep names
    sales_names = []
    for i in range(10):
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
    def coordinate_generator(area):
        """
        Generates a random location coordinates bettwen the given geographical limits of the area
        Area is a polygon generated by chosen locations
        """
        westernmost, southernmost, easternmost, northernmost = area.bounds
        random_point = Point(
            [
                round(random.uniform(westernmost, easternmost), 6),
                round(random.uniform(southernmost, northernmost), 6),
            ]
        )
        if random_point.within(area):
            # print(random_point)
            return {"lat": random_point.x, "lon": random_point.y}
        else:
            return coordinate_generator(area)

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

    for rep in sales_reps:
        rep.append(coordinate_generator(usa2))

    # Defining sales reps salary that equals 2000 + (500 x (experience / 5))
    for rep in sales_reps:
        rep.append(2000 + (500 * (rep[2] // 5)))

    # Defining clients random locations
    # Clients are defined by (number, location)
    clients = []
    for client in range(50):
        clients.append([client, coordinate_generator(usa)])

    return (sales_reps, clients)


if __name__ == "__main__":
    generate_data()
