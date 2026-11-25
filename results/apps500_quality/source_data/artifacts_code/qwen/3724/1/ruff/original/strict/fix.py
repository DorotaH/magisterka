def count_distinct_strings():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    S = data[1]

    MOD = 10**9 + 7

    # Initialize the dp array
    dp = [0] * (N + 1)
    dp[0] = 1

    # Initialize the prefix and suffix arrays
    prefix = [0] * (N + 1)
    suffix = [0] * (N + 1)

    # Initialize the count array
    count = [0] * 3

    # Initialize the result
    result = 0

    # Initialize the previous character
    prev = -1

    # Iterate over the string
    for i in range(N):
        # Get the current character
        c = ord(S[i]) - ord('A')

        # Update the prefix array
        prefix[i + 1] = (prefix[i] + count[(c + 1) % 3] + count[(c + 2) % 3]) % MOD

        # Update the count array
        count[c] += 1

        # Update the result
        result = (result + prefix[i + 1]) % MOD

        # Update the previous character
        prev = c

    # Print the result
    print(result)

count_distinct_strings()
