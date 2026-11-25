def find_cheating_move(n, k, a, m, shots):
    # Create a list to keep track of ship placements
    ships = [0] * n

    # Place the ships on the board
    for i in range(k):
        ships[i * a] = 1

    return next((i + 1 for i in range(m - 1, -1, -1) if ships[shots[i] - 1] == 0), -1)


# Read input
n, k, a = map(int, input().split())
m = int(input())
shots = list(map(int, input().split()))

# Find and print the cheating move
print(find_cheating_move(n, k, a, m, shots))
