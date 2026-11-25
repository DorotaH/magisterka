n, x, y = map(int, input().split())

# Calculate the minimum number of moves required for both kings to reach the coin
# The white king starts at (1,1) and the black king starts at (n,n)
# The maximum distance the white king can move in one move is sqrt(2) * (n-1)
# The maximum distance the black king can move in one move is sqrt(2) * (n-1)
# Therefore, the total maximum distance is 2 * sqrt(2) * (n-1)
# Since both kings move optimally, the total number of moves required is the minimum of these distances
# If the total number of moves is odd, the white king wins, otherwise the black king wins
if not (abs(x - 1) + abs(y - 1) + abs(n - x) + abs(n - y)) % 2 == 0:
    print("White")
else:
    print("Black")