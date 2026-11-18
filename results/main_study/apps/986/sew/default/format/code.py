n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
library = []
money = 0
for i in range(0, len(a)):
    if a[i] not in library:
        money += 1
        if not len(library) < k:
            curmin = n
            curindex = 0
            found = [n] * len(library)
            for j in range(len(a[i + 1 : :])):
                if (a[i + j + 1] in library) and (
                    found[library.index(a[i + j + 1])] == n
                ):
                    found[library.index(a[i + j + 1])] = j
            library[found.index(max(found))] = a[i]
        else:
            library.append(a[i])
print(money)
