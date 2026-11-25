import  sys

def  is_unique_crossword(n, x, a):
    # Calculate the total length of the crossword
    total_length = sum(a, 0)

    # Check if the total length matches the given length
    if  x != total_length:
        return "NO"

    # Check if the number of segments matches the given number
    if  len(a) != n:
        return "NO"

    # Sort the segments in descending order
    a.sort(reverse=True)

    # Initialize a variable to store the current position
    pos = 0

    # Iterate over the segments
    for  i in  range(n):
        # Check if the current segment can be placed at the current position
        if pos+a[i]>x:
            return  "NO"
        pos = pos + a[i]

    # If we have checked all segments and haven't returned "NO", the crossword is unique
    return  "YES"

# Read input from standard input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Print the result
print(is_unique_crossword(n, x, a))
