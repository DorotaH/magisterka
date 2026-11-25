
def solve():
    n, k=map(int, input().split())
    coins=list(map(int, input().split()))

    # Calculate the maximum possible value
    max_value=k

    # Create a set to store the possible values
    possible_values=set()

    # Iterate over all possible values from 0 to max_value
    for  i in  range(max_value + 1):
        dp = [False] * (1 + i)
        dp[0] = True

        # Try to make the current value with the given coins
        for  coin in  coins:
            for  j in  range(i, coin-1, -1):
                if dp[j - coin]:
                    dp[j] = True

        # If we can make the current value, add it to the set
        if  dp[i]:
            possible_values.add(i)

    # Print the number of possible values
    print(len(possible_values))

    # Print the possible values
    for  value in  sorted(list(possible_values)):
        print(value, end=' ')

if __name__=="__main__":
    solve()
