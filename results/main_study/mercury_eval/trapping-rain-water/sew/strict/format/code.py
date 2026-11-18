class Solution:
    def trap(self, height: List[int]) -> int:
        grids = height
        indexes = []

        for i in range(0, len(grids)):
            if not (grids[i] == 0):
                break
            else:
                indexes.append(i)
        for j in range(0, len(indexes)):
            grids.pop(0)

        indexes = []
        for i in range(len(grids) - 1, 0, -1):
            if not (grids[i] == 0):
                break
            else:
                indexes.append(i)
        for j in indexes:
            grids.pop(j)

        def getmaxfreq(temp):
            max_count = 1
            max_grid = max(temp)
            min_grid = min(temp)
            if min_grid == max_grid:
                return 0, 0
            if len(temp):
                while True:
                    temp.remove(max_grid)
                    if max_grid != max(temp):
                        break
                    else:
                        max_count += 1
            return (max_count, max_grid)

        litres = 0
        if len(grids) != 0 and len(grids) != 1:
            max_count, max_grid = getmaxfreq(grids.copy())
            if max_count == 0:
                return 0
            print(max_count, max_grid)
            pointer = grids[0]
            for i in range(len(grids) - 1):
                if pointer == max_grid and grids[i] == pointer:
                    pointer -= pointer - max(grids[1:])
                    max_grid = max(grids[1:])
                else:
                    break

            for gr in range(len(grids) - 1):
                if grids[gr + 1] == max_grid:
                    t = grids[gr + 2 :]
                    if len(t):
                        max1, min1 = max(t), min(t)
                        if min1 == max1:
                            return litres
                            break
                        if 1 == max_count:
                            max_count = max_count - 1
                            pointer = max1
                            max_count, max_grid = getmaxfreq(t)
                            continue
                        elif max_count > 1:
                            max_count -= 1
                            pointer = max_grid = max1
                            continue

                diff = pointer - grids[gr + 1]
                if diff < 0:
                    pointer = grids[gr + 1]
                elif diff > 0:
                    litres = litres + diff
                    continue

        return litres
