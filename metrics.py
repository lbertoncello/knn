import math

def euclidian_distance(u, v):
    distance = 0

    for i in range(len(u)):
        distance += (u[i] - v[i])**2

    distance = math.sqrt(distance)

    return distance