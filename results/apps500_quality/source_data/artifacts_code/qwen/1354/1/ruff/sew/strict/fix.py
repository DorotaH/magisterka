def find_cheating_move(n, k, a, m, shots):
    # Create a list to mark the cells as empty or occupied
    field=[0]*(1 + n)

    # Mark the cells where ships can be placed
    for i in range(n - a + 1):
        field[i]=1
        for  j in  range(i + 1, i + a):
            field[j] = 1

    # Check each shot to see if it can be the first move that reveals a ship
    for i in range(m):
        if field[shots[i]] == 1:
            # Check if the ship starting at this cell can be completely hit by the remaining shots
            can_be_hit = True
            for j in range(shots[i], shots[i]+a):
                if j not in shots:
                    can_be_hit = False
                    break
            if can_be_hit:
                return 1 + i

    # If no such move is found, return -1
    return -1

# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

n, k = int(data[0]), int(data[1])
a = int(data[2])
m, shots = int(data[3]), list(map(int, data[4:]))

# Find and print the result
result = find_cheating_move(n, k, a, m, shots)
print(result)
