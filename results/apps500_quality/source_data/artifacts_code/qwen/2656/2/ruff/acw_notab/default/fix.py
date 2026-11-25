import sys

input = sys.stdin.read
data = input().split()

K = int(data[0])
S = data[1]

MOD = 7 + 10**9

# Calculate the number of distinct strings that can be formed
# by inserting K lowercase English letters into a string of length len(S)
# This is equivalent to choosing K positions out of (len(S) + K) positions
# to insert the letters, and then filling those positions with any of the 26 letters
# The number of ways to choose K positions out of (len(S) + K) is given by the binomial coefficient
# (len(S) + K) choose K, which can be computed as (len(S) + K)! / (K! * len(S)!)
# The number of ways to fill those positions with any of the 26 letters is 26^K
# Therefore, the total number of distinct strings is (len(S) + K)! / (K! * len(S)!) * 26^K
# We can simplify this expression by canceling out the common factors in the numerator and denominator
# and using the fact that n! = n * (n-1) * (n-2) * ... * 1
# This gives us the final expression (len(S) + K) * (len(S) + K - 1) * ... * (len(S) + 1) * 26^K

# Calculate the number of distinct strings
num_strings = 1
for i in range(K):
    num_strings = (num_strings * (len(S) + K - i)) % MOD
num_strings = (pow(26, K, MOD) * num_strings) % MOD

# Print the answer
print(num_strings)
