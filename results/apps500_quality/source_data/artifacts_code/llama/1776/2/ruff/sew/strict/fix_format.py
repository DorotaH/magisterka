def calculate(expression, plus, minus):
    if not expression:
        return 0

    n = len(expression)
    dp = [[float("-inf")] * (plus + 1) for _ in range(minus + 1)]

    dp[0][0] = 0

    for i in range(0, n):
        for j in range(0, min(minus + 1, i + 1)):
            if expression[i] == "(":
                continue

            for k in range(min(plus, j) + 1):
                if expression[i] == "+":
                    dp[j][k] = max(dp[j][k], dp[j][k] + int(expression[i]))
                else:
                    dp[j][k] = max(dp[j][k], dp[j - 1][k] - int(expression[i]))

    result = float("-inf")
    for i in range(0, minus + 1):
        result = max(result, dp[i][plus])

    return result


def main():
    expression = input()
    plus, minus = map(int, input().split())
    print(calculate(expression, plus, minus))


if __name__ == "__main__":
    main()
