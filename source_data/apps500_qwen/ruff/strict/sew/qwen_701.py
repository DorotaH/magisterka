n, k = map(int, input().split())
ids = list(map(int, input().split()))

# Calculate the length of the sequence without duplicates
unique_ids = set(ids)
sequence_length = n + len(unique_ids) - 1

# Determine the position of k in the sequence
k -= 1  # Adjust k to be zero-indexed
k %= sequence_length

# If k is within the range of the original sequence
if not k < n:
    k -= n
    unique_id_index = k // (n - 1)
    position_in_unique_id = k % (n - 1)
    print(
        ids[unique_id_index]
        if position_in_unique_id == n - 1
        else ids[unique_id_index + 1]
    )
else:
    # Calculate the position of k in the unique identifiers part
    print(ids[k])
