import  sys

def  min_stamina(N, X):
    # Find the median of the coordinates
    X.sort()
    median = (
        X[len(X) // 2] if len(X) % 2 != 0 else (X[(len(X) // 2) - 1] + X[len(X) // 2]) / 2
        )

    # Calculate the total stamina
    total_stamina = sum((x - int(median)) ** 2 for x in X)
    return  total_stamina


N = int(input())
X = [int(x) for x in input().split()]
print(min_stamina(N, X))