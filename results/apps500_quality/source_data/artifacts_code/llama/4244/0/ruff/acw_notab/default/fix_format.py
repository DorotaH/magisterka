def min_stamina(N, X):
    # Find the median of the coordinates
    X.sort()
    median = (
        X[len(X) // 2] if len(X) % 2 != 0 else (X[len(X) // 2] + X[len(X) // 2 - 1]) / 2
    )

    return sum((x - int(median)) ** 2 for x in X)


N = int(input())
X = [int(x) for x in input().split()]
print(min_stamina(N, X))
