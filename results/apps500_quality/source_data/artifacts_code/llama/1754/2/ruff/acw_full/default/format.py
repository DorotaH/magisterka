import sys


def main():
    n, m, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))
    c = list(map(int, input().split()))

    school_max = {}
    for i in range(n):
        school_max[s[i]] = max(school_max.get(s[i], 0), p[i])

    chosen_max = {}
    for c_i in c:
        chosen_max[s[c_i - 1]] = max(chosen_max.get(s[c_i - 1], 0), p[c_i - 1])

    made_up = sum(
        bool(school not in school_max or value > school_max[school])
        for school, value in chosen_max.items()
    )
    print(made_up)


if __name__ == "__main__":
    main()
