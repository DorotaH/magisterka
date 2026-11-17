import math
import random
import statistics

# Constants
RADIUS = 5


def task_func(n):
    """
    Generate n random points within a circle of radius RADIUS (default value is 5) and return their average distance from the center.

    Parameters:
    - n (int): The number of points to be generated.

    Returns:
    - float: The average distance from the center of the circle.

    Requirements:
    - math
    - random
    - statistics

    Example:
    >>> random.seed(42)
    >>> task_func(100)
    3.2406
    >>> task_func(50)
    3.4443
    """
    distances = list()

    for _ in range(n):
        theta, r = 2 * math.pi * random.random(), RADIUS * math.sqrt(random.random())
        x, y = r * math.cos(theta), r * math.sin(theta)
        distance = math.sqrt(pow(x, 2) + pow(y, 2))
        distances.append(distance)

    return round(statistics.mean(distances), 4)
