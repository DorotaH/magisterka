from math import acos, cos, sin


def distance_lat_long(slat, slon, elat, elon):
    return 6371.01 * acos(
        sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon)
    )
