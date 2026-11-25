# Read input
N, A = int(input()), list(map(int, input().split()))

# Sort the array to facilitate finding pairs
A.sort()

# Initialize the maximum area
max_area = 0

# Use a set to keep track of visited elements
visited = set()

# Iterate over each element in the array
for i in range(N):
    if A[i] in visited:
        continue
    visited.add(A[i])

    # Check for the maximum possible pair
    for j in range(N - 1, i, -1):
        if A[j] in visited:
            continue
        visited.add(A[j])

        # Check if the sum of the current pair is greater than the maximum area found so far
        if A[i] + A[j] > max_area:
            # Check for the smallest pair that can form a rectangle with the current pair
            for k in range(i + 1, N):
                if A[k] in visited:
                    continue
                visited.add(A[k])

                # Check if the sum of the current pair is greater than the maximum area found so far
                if A[i] + A[j] > max_area:
                    # Check if the smallest pair that can form a rectangle with the current pair
                    for l in range(k + 1, N):
                        if A[l] in visited:
                            continue
                        visited.add(A[l])

                        # Check if the sum of the current pair is greater than the maximum area found so far
                        if A[i] + A[j] > max_area:
                            # Check if the smallest pair that can form a rectangle with the current pair
                            if A[j] * A[i] > max_area:
                                max_area = A[j] * A[i]
                                break
                    break
                break
            break

# Print the maximum possible area of the rectangle
print(max_area)
