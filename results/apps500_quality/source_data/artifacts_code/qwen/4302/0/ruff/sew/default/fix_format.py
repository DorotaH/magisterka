A, B = map(int, input().split())

# Calculate the maximum coins by pressing the button of size A twice
max_coins = 2 * A

# Calculate the maximum coins by pressing the button of size B twice
max_coins = max(max_coins, 2 * B)

# Calculate the maximum coins by pressing both buttons once
max_coins = max(max_coins, A + B)

print(max_coins)
