

def count_games(n, c, a):
    # Initialize count of games bought
    bought = 0

    # Initialize index of current game and bill
    game_index = 0
    bill_index = 0

    # Traverse games and bills
    while game_index < n and bill_index < len(a):
        # If current game can be bought with current bill, buy it
        if c[game_index] <= a[bill_index]:
            bought += 1
            game_index += 1
        # Move to the next bill
        bill_index += 1

    # Return count of games bought
    return bought


# Read input from standard input
n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

# Print result
print(count_games(n, c, a))
