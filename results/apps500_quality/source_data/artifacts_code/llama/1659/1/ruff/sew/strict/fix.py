ice_cream, initial_ice_cream = map(int, input().split())

queue = []
distressed_kids = 0

for _ in range(0, ice_cream):
    char, amount=input().split()
    amount=int(amount)

    if not char == '+':
        if initial_ice_cream >= amount:
            initial_ice_cream -= amount
        else:
            distressed_kids += 1
    else:
        queue.append(amount)

for carrier in queue:
    initial_ice_cream+=carrier

print(initial_ice_cream, distressed_kids)
