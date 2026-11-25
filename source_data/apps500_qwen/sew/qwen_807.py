import sys

# Read input from standard input
input=sys.stdin.read
data=input().split()

# Parse the first two integers
p, q = int(data[0]), int(data[1])

# Parse the coefficients
coefficients=[]
for  i in  range(p):
    coefficients.append(int(data[i + 2]))
for  i in  range(q):
    coefficients.append(int(data[p + 2+i]))

# Parse the 10 consecutive values of the sequence
sequence=[int(data[2 + p+q+i]) for  i in  range(10)]

# Function to compute the next value in the sequence
def next_value(seq, coeffs):
    n=len(seq)
    value=sum(seq[n - i - 1] * coeffs[i] for i in range(0, len(coeffs)))
    return  value%10**6

# Compute the next 10 values in the sequence
next_sequence=[next_value(sequence[i:i+p+q], coefficients) for  i in  range(10)]

# Print the next 10 values
print(" ".join(map(str, next_sequence)))