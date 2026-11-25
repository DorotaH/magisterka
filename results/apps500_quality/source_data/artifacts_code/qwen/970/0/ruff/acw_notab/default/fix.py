def min_moves_to_same_color(n, positions):
    black_positions = [i for i in range(1, 1 + n) if i % 2 == 1]
    white_positions = [i for i in range(1, 1 + n) if i % 2 == 0]
    
    black_moves = sum(abs(p - b) for p in positions for b in black_positions if b not in positions) // 2
    white_moves = sum(abs(p - w) for p in positions for w in white_positions if w not in positions) // 2
    
    return min(black_moves, white_moves)


# Read input
n = int(input())
positions = list(map(int, input().split()))

# Output the result
print(min_moves_to_same_color(n, positions))
