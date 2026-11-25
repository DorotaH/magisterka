from collections import defaultdict


def main():
    m, k, n, s = map(int, input().split())
    flower_types, required_types = (
        list(map(int, input().split())),
        list(map(int, input().split())),
    )

    flower_counts, required_counts = defaultdict(int), defaultdict(int)

    for t in required_types:
        required_counts[t] += 1

    for i in range(0, s):
        flower_counts[required_types[i]] += 1

    for t in flower_types:
        flower_counts[t] += 1

    flower_counts = sorted(flower_counts.items(), key=lambda x: x[1], reverse=True)

    min_required_flowers = sum(required_counts.values())

    start, end = 0, m - k

    while start <= end:
        max_removal = start
        for i in range(0, s):
            req, cnt = required_types[i], required_counts[required_types[i]]
            while flower_counts[req] < cnt and start <= end:
                max_removal = max(max_removal, start + (k * (flower_counts[req] - cnt)))
                start += 1
                flower_counts[req] -= 1
            if flower_counts[req] < cnt:
                break
        else:
            if max_removal >= start + (end - start + 1) * k - min_required_flowers:
                print(end - start + 1)
                removals = sorted([i + 1 for i in range(start, end + 1)])
                print(" ".join(map(str, removals)))
                return None
            max_removal = min(max_removal, end - k)
            end = max_removal - 1

    print(-1)


if __name__ == "__main__":
    main()
