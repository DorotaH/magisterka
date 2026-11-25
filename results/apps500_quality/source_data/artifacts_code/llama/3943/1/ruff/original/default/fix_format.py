a, b = map(int, input().split())

if a == 0:
    print(-b * b)
    print("x" * b)
elif b == 0:
    print(a * a)
    print("o" * a)
else:
    if a > b:
        max_score = 0
        max_config = ""
        for k in range(a + 1):
            score = 0
            config = ""
            for i in range(a + b):
                if i >= k:
                    config += "x"
                    score -= (i - k + 1) ** 2
                else:
                    config += "o"
                    score += (a - k + i) ** 2
            if score > max_score:
                max_score = score
                max_config = config
        print(max_score)
        print(max_config)
    else:
        print(a * a - b * b)
        print("o" * a + "x" * b)
