from typing import List


def can_form_tree(n: int, d: int, k: int) -> List[str]:
    if d > 2 * k:
        return ["NO"]

    if d == 1:
        return ["YES"] + [f"{i} {i + 1}" for i in range(1, n)]

    if d == 2:
        return ["YES"] + [f"1 {i}" for i in range(2, 1 + n)] + [f"2 {n}"]

    if d == 3:
        return (
            ["YES"]
            + [f"1 {i}" for i in range(2, n // 2 + 1)]
            + [f"{n // 2} {n}"]
            + [f"2 {n // 2 + 1}"]
            + [f"{n // 2 + 1} {n - 1}"]
            + [f"{n - 1} {n}"]
        )

    if d == 4:
        return (
            ["YES"]
            + [f"1 {i}" for i in range(2, n // 2 + 1)]
            + [f"{n // 2} {n}"]
            + [f"2 {n // 2 + 1}"]
            + [f"{n // 2 + 1} {n - 1}"]
            + [f"{n - 1} {n}"]
            + [f"2 {2 + n // 2}"]
            + [f"{2 + n // 2} {n - 2}"]
            + [f"{n - 2} {n}"]
        )

    return ["NO"]


# Read input
n, d, k = map(int, input().split())

# Generate and print the result
result = can_form_tree(n, d, k)
if result[0] == "NO":
    print("NO")
else:
    print("YES")
    for line in result[1:]:
        print(line)
