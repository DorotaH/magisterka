class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n < 2:
            if k == 0:
                return 1
            else:
                return 0
        # all forwarded case
        if k == 0:
            return 1
        maxK = n * (n - 1) // 2
        if k > maxK:
            return 0
        # all reversed case
        if k == maxK:
            return 1

        # speed up
        # print(k, ' --> ', (maxK // 2) - k, 'for maxK = ', maxK)
        if n > 100 and k > 100 and k > maxK // 2:
            k = (maxK // 2) - k

        # allocate two lines
        cnt, mod = [[0 for k in range(maxK + 1)] for r in range(2)], 1000000000 + 7

        # init (# of elements == 2 case)
        prev, cur = 0, 1

        cnt[prev][0] = 1
        cnt[prev][1] = 1

        for nn in range(3, n + 1):
            kkMax = nn * (nn - 1) // 2
            halfMax = kkMax // 2
            for kk in range(kkMax + 1):
                #
                # we don't need it, speed up
                #
                if k < kk:
                    break
                if kk in (0, kkMax):
                    cnt[cur][kk] = 1
                elif halfMax < kk:
                    cnt[cur][kk] = cnt[cur][kkMax - kk]
                else:
                    if not kk < nn:
                        cnt[cur][kk] = (
                            cnt[cur][kk - 1] + cnt[prev][kk] - cnt[prev][kk - nn]
                        ) % mod
                    else:
                        # we added more than nn elements, so subtract left end
                        cnt[cur][kk] = (cnt[cur][kk - 1] + cnt[prev][kk]) % mod

                if nn == n and kk == k:
                    return cnt[cur][kk]
            # print(nn, ':', cnt[cur][:kkMax+1])
            prev = 1 - prev
            cur = 1 - cur
        pass
