a, b, c, d = map(int, input().split())

start_time, alice_start = 0, a
alice_end, bob_start = b, c
bob_end = d

# Find the overlap of Alice's and Bob's button presses
overlap_start, overlap_end = (
    max(start_time, alice_start, bob_start),
    min(alice_end, bob_end),
)

# Calculate the length of the overlap
overlap_length = max(0, overlap_end - overlap_start)

print(overlap_length)
