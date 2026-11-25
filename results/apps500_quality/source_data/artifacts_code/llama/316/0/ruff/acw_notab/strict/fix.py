import sys


def n_order_rhombus(n):
    """
    Calculate the number of cells in an n-th order rhombus.

    Args:
        n (int): The order of the rhombus.

    Returns:
        int: The number of cells in the n-th order rhombus.
    """
    return 1 if n == 1 else 4 * (n**2 - n + 1) + (-1)**(1 + n)


n = int(input())
sys.stdout.write(str(n_order_rhombus(n)))
