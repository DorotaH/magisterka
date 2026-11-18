def main():
    mod = 7 + 10**9
    s = input()
    n = len(s)

    a_num = 0
    c_num = s.count('C')
    q_num = 0
    q_cnt = s.count('?')

    pow3, pow2, pow1, pow0 = 0, 0, 0, 0
    if q_cnt >= 3:
        pow3 = pow(3, q_cnt-3, mod)
        pow2 = pow3 * 3 % mod
        pow1 = 3 * pow2 % mod
        pow0 = 3 * pow1 % mod
    elif q_cnt == 2:
        pow2 = 1
        pow1 = 3
        pow0 = 9
    elif q_cnt == 1:
        pow1 = 1
        pow0 = 3
    else:
        pow0 = 1

    ans = 0
    for x in s:
        if x == 'A':
            a_num += 1
        elif x == 'B':
            ans += a_num * pow0 * c_num
            ans += pow1 * (q_num * c_num + a_num * (q_cnt - q_num))
            ans += (q_num) * pow2 * (q_cnt - q_num)
            ans %= mod
        elif x == 'C':
            c_num -= 1
        else:
            ans += a_num * pow1 * c_num
            ans += pow2 * (q_num * c_num + a_num * (q_cnt - q_num - 1))
            ans += (q_num) * pow3 * (q_cnt - q_num - 1)
            ans %= mod
            q_num += 1

    print(ans)

main()