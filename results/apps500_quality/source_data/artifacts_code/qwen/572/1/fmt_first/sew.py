def  count_ways_to_change(n, k, coefficients):
    # Calculate P(2)
    P_2=sum(a*2**i for  i, a in  enumerate(coefficients, 0))

    # Initialize the count of valid ways
    count=0

    # Iterate over each coefficient and its position
    for  i, a in  enumerate(coefficients, 0):
        # Calculate the required change to make P(2) = 0
        required_change=P_2

        # If the coefficient is not the leading coefficient, we need to adjust for x^i
        if  i != n:
            required_change -= a * 2**i

        # Calculate the possible new values for the coefficient
        for new_value in range(-k, k + 1):
            if abs(new_value-a)<=k:
                # Check if the new polynomial is valid and Q(2) = 0
                if  (
                    coefficients[n] != new_value
                    and  (required_change + new_value * (2**i)) % (2 ** (i + 1)) == 0
                    ):
                    count = count + 1

    return  count


# Read input
n, k=map(int, input().split())
coefficients=list(map(int, input().split()))

# Print the result
print(count_ways_to_change(n, k, coefficients))
