
def calculate_depth(H, L):
    """
    Calculate the depth of the lake at point A.

    Parameters:
    H (float): The height of the water lily above the water surface.
    L (float): The horizontal distance from the point where the lily touched the water to the point where Inessa picked it up.

    Returns:
    float: The depth of the lake at point A.
    """
    return  H + (L - H) / 2

def main():
    # Read input from standard input
    H, L = map(int, input().split())

    # Calculate the depth of the lake at point A
    depth = calculate_depth(H, L)

    # Print the result to standard output
    print(f"{depth:.10f}")


if  __name__ == "__main__":
    main()