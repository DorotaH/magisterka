
def solve():
    n, U = map(int, input().split())
    E = list(map(int, input().split()))

    max_eff = -1

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if E[k] - E[i] <= U:
                    efficiency = (E[k] - E[j]) / (E[k] - E[i])
                    max_eff = max(max_eff, efficiency)

    if max_eff == -1:
        print(-1)
    else:
        print(format(max_eff, ".9f"))

if __name__ == "__main__":
    solve()
