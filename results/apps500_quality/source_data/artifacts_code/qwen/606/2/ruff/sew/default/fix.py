import math
import sys


def  main():
    # Read input
    R, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    # Calculate the distance between the center of the flat and Fafa's laptop
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Calculate the radius of the access point
    r = distance - R
    
    # If the radius is negative, it means Fafa's laptop is inside the flat
    r = max(r, 0)
    
    # Calculate the position of the access point
    x_ap = x1 + (x2 - x1) * (R / (R + r))
    y_ap = y1 + (y2 - y1) * (R / (R + r))
    
    # Print the result
    print(f"{x_ap} {y_ap} {r}")

if __name__=="__main__":
    main()
