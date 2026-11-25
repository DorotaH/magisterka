def  find_cheating_move(n, k, a, m, shots):
    # Create a list to keep track of ship placements
    ships=[0]*n
    
    # Place the ships on the board
    for  i in  range(k):
        ships[a * i] = 1
    
    # Iterate through the shots in reverse order to find the cheating move
    for  i in  range(m - 1, -1, -1):
        if  ships[shots[i] - 1] == 0:
            return i + 1
    
    # If no cheating move is found, return -1
    return -1

# Read input
n, k, a = map(int, input().split())
m = int(input())
shots = list(map(int, input().split()))

# Find and print the cheating move
print(find_cheating_move(n, k, a, m, shots))
