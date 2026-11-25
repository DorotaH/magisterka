

def  count_xorangles(n):
    # Initialize a list to store the number of xorangles for each possible xor-sum
    xor_sums=[0]*(n * 2 + 1)
    xor_sums[0]=1  # There is one way to have xor-sum equal to 0 (no sides)

    # For each possible length of the first side (from 1 to n)
    for a in range(1, 1 + n):
        # For each possible length of the second side (from a to n)
        for  b in  range(a, n):
            # Calculate the xor-sum of the first two sides
            xor_sum=a^b
            # For each possible length of the third side (from max(a, b) to n)
            for  c in  range(max(a, b), 1 + n):
                # If the xor-sum of all three sides is zero
                if xor_sum == 0:
                    # Increment the count of xorangles
                    xor_sums[a ^ c] += 1

    # The total number of xorangles of order n is the sum of the number of xorangles
    # with xor-sums from 0 to n (exclusive)
    return  sum(xor_sums[n - (n % 2):], 0)

# Read the input from standard input
n=int(input())

# Print the result
print(count_xorangles(n))
