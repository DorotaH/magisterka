import sys
import math


def main():
    # Read input from standard input
    input=sys.stdin.read
    data=input().split()

    # Convert input data to integers
    A = []
    for x in data:
        A.append(int(x))

    # Sort the array to find the minimum cost
    A.sort()

    # The minimum cost to complete all tasks is the sum of the absolute differences
    # between consecutive elements in the sorted array
    min_cost=0
    for  i in  range(1, len(A)):
        min_cost = min_cost + abs(A[i] - A[i - 1])

    # Print the minimum cost
    print(min_cost)


if  __name__=="__main__":
    main()
