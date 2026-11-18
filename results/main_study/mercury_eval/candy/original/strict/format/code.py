class Solution:
    def candy(self, ratings: List[int]) -> int:
        increase = []
        decrease = []
        cnt_inc = 1
        cnt_dec = 1
        n = len(ratings)

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                cnt_inc += 1
                decrease.append(cnt_dec)
                cnt_dec = 1
            elif ratings[i - 1] > ratings[i]:
                cnt_dec += 1
                increase.append(cnt_inc)
                cnt_inc = 1
            else:
                increase.append(cnt_inc)
                cnt_inc = 1
                decrease.append(cnt_dec)
                cnt_dec = 1

        increase.append(cnt_inc)
        decrease.append(cnt_dec)

        inc_arr = []
        for m in increase:
            i = 0
            e = 1
            while i < m:
                inc_arr.append(e)
                e += 1
                i += 1

        dec_arr = []
        for m in decrease:
            i = 0
            e = m
            while i < m:
                dec_arr.append(e)
                e -= 1
                i += 1

        ans = []
        for i in range(n):
            ans.append(max(inc_arr[i], dec_arr[i]))

        return sum(ans)
