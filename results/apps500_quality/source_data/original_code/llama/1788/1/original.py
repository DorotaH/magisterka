import sys

def find_X_Y():
    # Read input from standard input
    A, B = map(int, input().split())

    # Calculate X and Y using the given equations: X + Y = A and X - Y = B
    X = (A + B) // 2
    Y = A - X

    # Print the result
    print(X, Y)

if __name__ == "__main__":
    find_X_Y()
