from typing import List, Tuple

def  calculate_traffic(n: int, m: int, levels: List[List[str]], w: int) -> Tuple[int, List[Tuple[int, int]]]:
    k = len(levels)
    total_traffic = 0
    transfer_plan = []
    previously_transmitted = [-1] * k
    
    for i in range(k):
        if not i == 0:
            min_traffic = float('inf')
            best_diff = -1
            best_prev = -1
            for j in range(i):
                diff = sum(levels[i][r][c] != levels[j][r][c] for r in range(n) for c in range(m))
                traffic = diff * w + n * m
                if traffic < min_traffic:
                    min_traffic = traffic
                    best_diff = diff
                    best_prev = j
            total_traffic += min_traffic
            transfer_plan.append((i + 1, best_prev + 1))
            previously_transmitted[i] = best_prev
        else:
            total_traffic += n * m
            transfer_plan.append((i + 1, 0))
            previously_transmitted[i] = i
    
    return (total_traffic, transfer_plan)

def  main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    w = int(data[3])
    
    levels = []
    index = 4
    for _ in range(k):
        level = []
        for i in range(n):
            level.append(list(data[index + i]))
        levels.append(level)
        index = index + n
    
    total_traffic, transfer_plan = calculate_traffic(n, m, levels, w)
    
    print(total_traffic)
    for plan in transfer_plan:
        print(plan[0], plan[1])

if __name__ == "__main__":
    main()