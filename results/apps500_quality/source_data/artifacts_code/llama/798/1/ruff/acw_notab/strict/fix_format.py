def can_build_molecule(valences):
    a, b, c = valences
    if a + b + c != sum(valences):
        return "Impossible"
    if a == 2 and b == 2 and c == 2:
        return "Impossible"
    if a % 2 == b % 2 and a % 2 == c % 2 and a != b and a != c:
        return "1 1 1"
    if a % 2 == b % 2 and a % 2 != c % 2:
        return f"{int((b + c) / 2)} {int((b + c) / 2)} 0"
    if a % 2 != b % 2 and a % 2 == c % 2:
        return f"0 {int((a + b) / 2)} {int((a + c) / 2)}"
    if a % 2 == c % 2 and b % 2 == a:
        return f"{int((a + c) / 2)} 0 {int((a + b) / 2)}"
    if a % 2 == c % 2 and b % 2 == b:
        return f"{int((a + c) / 2)} {int((b + c) / 2)} 0"
    if a % 2 != b % 2:
        return f"{int((a + b) / 2)} {int((b + c) / 2)} {int((a + c) / 2)}"


valences = list(map(int, input().split()))
print(can_build_molecule(valences))
