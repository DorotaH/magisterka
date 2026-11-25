import  sys

def largest_perfect_power(X):
    max_power=0
    for  b in  range(1, X + 1):
        p = 2
        while  True:
            power=pow(b, p)
            if  X < power:
                break
            if  max_power < power:
                max_power = power
            p += 1
    return max_power

# Read input
X = int(sys.stdin.read().strip())

# Print the result
print(largest_perfect_power(X))
