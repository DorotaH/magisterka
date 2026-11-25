

def main():
    d, L, v1, v2 = map(float, input().split())
    v = v2 + v1
    t = (L - d) / v
    left = (L - d) / (v2 + v1)
    right = (L - d) / (v2 + v1)
    t = min(t, left, right)
    print(t)


if __name__ == "__main__":
    main()
