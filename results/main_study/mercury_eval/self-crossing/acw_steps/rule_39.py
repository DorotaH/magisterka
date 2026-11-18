class Solution:
    def isSelfCrossing(self, arr: List[int]) -> bool:
        if len(arr) < 4: return False
        lines, parallel = defaultdict(set), defaultdict(set)   #x/y: interval
        x = y = 0
        lines[0].add((0,arr[0]))
        y += arr[0]
        parallel[y].add((-arr[1],0))
        x -= arr[1]
        prev = x,(y-arr[2],y)
        y -= arr[2]

        out = y < 0
        for i,n in enumerate(arr[3:], start=3):
            if i%2 == 0:
                pos = x
                if i%4 == 0:
                    y += n
                    start, end = y-n, y
                else:
                    y -= n
                    start, end = y, y+n
            else:
                pos = y
                if i%4 == 1:
                    x -= n
                    start, end = x, x+n
                else:
                    x += n
                    start, end = x-n, x

            if arr[i-2] >= n:
                out = False

            if not out:
                for k in lines:
                    for l,r in lines[k]:
                        if start <= k <= end and l <= pos <= r:
                            return True

                for l,r in parallel[pos]:
                    if start <= r and l <= end:
                        return True

            lines[prev[0]].add(prev[1])
            prev = pos,(start,end)
            lines, parallel = parallel, lines
        return False