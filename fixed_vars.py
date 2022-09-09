from adittional_functions import *

# Defining minimum driving distance between sales_rep and client
min_distance = 10800

sales_rep_fixed = (
    ["Liz Mills", 5, 23, {"lat": 39.108036, "lon": -111.203385}],
    ["Sheila Hersha", 1, 1, {"lat": 39.183247, "lon": -112.050574}],
    ["Lisa Deboer", 5, 21, {"lat": 37.520187, "lon": -109.841701}],
    ["Bret Warren", 1, 25, {"lat": 39.711014, "lon": -111.059193}],
    ["Leah Chugg", 4, 6, {"lat": 37.384121, "lon": -110.460507}],
    ["Leona Philip", 2, 19, {"lat": 40.158574, "lon": -112.543115}],
    ["Evangeline Richardson", 3, 21, {"lat": 37.511001, "lon": -110.052423}],
    ["Mary Bray", 1, 9, {"lat": 39.21669, "lon": -111.707886}],
    ["Louis Wolley", 4, 20, {"lat": 40.382913, "lon": -109.61324}],
    ["Clara Wright", 4, 20, {"lat": 37.405826, "lon": -113.303807}],
    ["Jose Lugo", 3, 24, {"lat": 39.799294, "lon": -109.699827}],
    ["Betty Rodriguez", 5, 4, {"lat": 41.355566, "lon": -111.961381}],
    ["Abby Smith", 5, 19, {"lat": 37.858953, "lon": -113.03345}],
    ["Christopher Benford", 2, 5, {"lat": 39.817606, "lon": -113.535048}],
    ["Pedro Markle", 4, 8, {"lat": 37.234962, "lon": -110.264661}],
    ["Charlotte Sisco", 5, 10, {"lat": 40.357361, "lon": -110.585693}],
    ["Beverly Nguyen", 5, 8, {"lat": 37.492833, "lon": -112.29737}],
    ["Diane Armenta", 1, 5, {"lat": 40.287017, "lon": -113.435624}],
    ["Howard Reed", 5, 14, {"lat": 40.562723, "lon": -113.741655}],
    ["Hope Parker", 5, 17, {"lat": 39.722351, "lon": -110.832073}],
    ["Johnny Wallace", 2, 11, {"lat": 37.099866, "lon": -113.539417}],
    ["Howard Coe", 2, 10, {"lat": 37.419166, "lon": -113.596784}],
    ["Reta Cummings", 2, 3, {"lat": 37.799432, "lon": -111.923134}],
    ["Claudia Savarese", 5, 22, {"lat": 38.758166, "lon": -111.943644}],
    ["David Vargas", 3, 5, {"lat": 37.291369, "lon": -110.934005}],
    ["Chad Davis", 4, 25, {"lat": 39.269413, "lon": -111.614398}],
    ["William Corda", 5, 13, {"lat": 37.877487, "lon": -111.111438}],
    ["Lauren Sharp", 4, 25, {"lat": 40.717653, "lon": -111.263192}],
    ["Mary Cannon", 3, 25, {"lat": 39.904714, "lon": -110.866214}],
    ["Brandon Tuley", 2, 22, {"lat": 41.395206, "lon": -113.362887}],
    ["Terry Heald", 4, 10, {"lat": 37.562065, "lon": -113.751457}],
    ["Norma Crowe", 5, 11, {"lat": 39.878011, "lon": -113.559814}],
    ["Steve Lawrence", 1, 24, {"lat": 39.368952, "lon": -111.550484}],
    ["Frank Anderson", 2, 23, {"lat": 37.790422, "lon": -110.604292}],
    ["Sophie Rumberger", 4, 15, {"lat": 38.925605, "lon": -109.074839}],
    ["Kenneth Brock", 5, 22, {"lat": 39.136043, "lon": -111.114217}],
    ["Carolyn Averette", 2, 4, {"lat": 40.277925, "lon": -112.29317}],
    ["Anna Chandler", 1, 22, {"lat": 41.67118, "lon": -113.693296}],
    ["Matthew Mccartney", 4, 7, {"lat": 38.855179, "lon": -110.494801}],
    ["Jon Kissell", 3, 15, {"lat": 40.628489, "lon": -110.36216}],
    ["William Kendall", 5, 8, {"lat": 37.764673, "lon": -112.910631}],
    ["Jeff Scharfenberg", 1, 7, {"lat": 40.42877, "lon": -111.694353}],
    ["James Harvey", 1, 9, {"lat": 38.058149, "lon": -113.198568}],
    ["Brenda Purdy", 2, 23, {"lat": 37.328093, "lon": -111.212597}],
    ["Marguerite Welsh", 4, 11, {"lat": 40.615239, "lon": -109.983683}],
    ["Frank Dickey", 1, 18, {"lat": 37.086706, "lon": -112.635552}],
    ["Ivan Bernal", 4, 24, {"lat": 41.934994, "lon": -112.849529}],
    ["Vivian Blanks", 1, 3, {"lat": 37.169817, "lon": -111.391887}],
    ["Meagan Ansel", 5, 7, {"lat": 38.055532, "lon": -109.915189}],
    ["Elizabeth Damato", 3, 6, {"lat": 37.479378, "lon": -110.738018}],
)

clients_fixed = (
    [0, {"lat": 37.283974, "lon": -110.570534}],
    [1, {"lat": 37.386595, "lon": -111.949458}],
    [2, {"lat": 39.044547, "lon": -112.637757}],
    [3, {"lat": 37.881421, "lon": -110.235337}],
    [4, {"lat": 39.650528, "lon": -109.247585}],
)

"""for rep in sales_rep_fixed:
    for client in clients_fixed:
        dst = driving_time(
            rep[3]["lat"],
            rep[3]["lon"],
            client[1]["lat"],
            client[1]["lon"],
        )
        if dst <= min_distance:
            print("Possible")"""
