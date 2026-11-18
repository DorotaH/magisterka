class Solution:
    def  nearestPalindromic(self, n: str) -> str:
        n_len, n_int = len(n), int(n)

        base = n[:(n_len + 1) // 2]
        base_int = int(base)

        def make_pal(x):
            sx = str(x)
            return  int(sx+sx[:len(sx) - n_len % 2][::-1])

        candidates = (
            [10 ** (n_len - 1) - 1] +
            [make_pal(base_int + i) for  i in  (-1, 0, 1)] +
            [1 + 10 ** n_len]
        )

        candidates_non_self = [cand for cand in candidates if cand != n_int]

        ans = min(candidates_non_self, key=lambda  x: abs(x - n_int))
        return str(ans)
