k, n, s, p = map(int, input().split())

required_sheets = k * n
sheets_per_pack = p * s
total_packs = -(-required_sheets // sheets_per_pack)  # ceiling division in Python

print(total_packs)
