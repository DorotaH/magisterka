import math
def largest_triangle(a,b): 
    return -1 if (a < 0 or b < 0) else (3 * math.sqrt(3) * pow(a, 2)) / (4 * b) 