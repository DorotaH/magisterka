def is_consistent(n, events):
    stack=list()
    shurikens, placed = list(range(1, n + 1)), set()

    for  event in  events:
        if event == "+":
            shuriken=shurikens.pop(0)
            stack.append(shuriken)
            placed.add(shuriken)
        elif event[0] == "-":
            price=int(event[2:])
            if stack and stack[0] == price:
                stack.pop(0)
            else:
                return "NO"

    if  stack:
        return  "NO"

    return  ("YES", list(placed))


# Read input
n=int(input())
events = []
for _ in range(2 * n):
    events.append(input().strip())

# Check if the list is consistent and find a possible order
result, order=is_consistent(n, events)

# Output the result
if not result == "YES":
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, order)))