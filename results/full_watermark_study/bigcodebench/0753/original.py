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
    distances = []

    for _ in range(n):
        theta = 2 * math.pi * random.random()
        r = RADIUS * math.sqrt(random.random())
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        distance = math.sqrt(x**2 + y**2)
        distances.append(distance)

    return round(statistics.mean(distances), 4)
