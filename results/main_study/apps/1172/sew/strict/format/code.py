def main():
    mod, s = 10**9 + 7, input()
    n = len(s)

    a_num, c_num = 0, s.count("C")
    q_num, q_cnt = 0, s.count("?")

    pow3, pow2, pow1, pow0 = 0, 0, 0, 0
    if q_cnt >= 3:
        pow3 = pow(3, q_cnt - 3, mod)
        pow2 = 3 * pow3 % mod
        pow1 = 3 * pow2 % mod
        pow0 = 3 * pow1 % mod
    elif 2 == q_cnt:
        pow2, pow1 = 1, 3
        pow0 = 9
    elif 1 == q_cnt:
        pow1, pow0 = 1, 3
    else:
        pow0 = 1

    ans = 0
    for x in s:
        if x == "A":
            a_num += 1
        elif x == "B":
            ans = ans + pow0 * a_num * c_num
            ans = ans + pow1 * (q_num * c_num + a_num * (q_cnt - q_num))
            ans = ans + pow2 * (q_num) * (q_cnt - q_num)
            ans = ans % mod
        elif x == "C":
            c_num = c_num - 1
        else:
            ans = ans + pow1 * a_num * c_num
            ans = ans + pow2 * (q_num * c_num + a_num * (q_cnt - q_num - 1))
            ans = ans + pow3 * (q_num) * (q_cnt - q_num - 1)
            ans = ans % mod
            q_num = q_num + 1

    print(ans)


main()
