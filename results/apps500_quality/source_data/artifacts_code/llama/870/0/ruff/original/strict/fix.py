
def main():
    d, L, v1, v2 = map(float, input().split())
    v = v1 + v2
    t = (L - d) / v
    left = (L - d) / (v1 + v2)
    right = (L - d) / (v1 + v2)
    t = min(t, left, right)
    print(t)

if __name__ == "__main__":
    main()
