number = int(input())
for i in range(number):
    chislo = int(input())
    if not chislo % 2 == 1:
        if chislo % 3 == 1:
            print(3, chislo - 1)
        elif chislo % 3 == 2:
            print(3, chislo - 2)
    else:
        print(2, chislo - 1)
