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

    made_up = 0
    for school in chosen_max:
        if school not in school_max or chosen_max[school] > school_max[school]:
            made_up += 1

    print(made_up)

if __name__ == "__main__":
    main()
