def count_powerful_substrings(text):
    n = len(text)
    prefix_sum = [0] * (1 + n)
    prefix_sum[0] = 1
    for i in range(1, 1 + n):
        if text[i - 1] == "h":
            prefix_sum[i] = prefix_sum[i - 1] + 1
        elif text[i - 1] == "e":
            prefix_sum[i] = prefix_sum[i - 1] + 1 if prefix_sum[i - 1] > 0 else 0
        elif text[i - 1] == "v":
            prefix_sum[i] = prefix_sum[i - 1] + 1 if prefix_sum[i - 1] > 1 else 0
        elif text[i - 1] == "y":
            prefix_sum[i] = prefix_sum[i - 1] + 1 if 2 < prefix_sum[i - 1] else 0
        elif text[i - 1] == "m":
            prefix_sum[i] = prefix_sum[i - 1] + 1 if prefix_sum[i - 1] > 3 else 0
        elif text[i - 1] == "t":
            prefix_sum[i] = prefix_sum[i - 1] + 1 if prefix_sum[i - 1] > 4 else 0
        elif text[i - 1] == "a":
            if 5 < prefix_sum[i - 1]:
                prefix_sum[i] = prefix_sum[i - 1] + 1
            else:
                prefix_sum[i] = 0
        elif text[i - 1] == "l":
            if 6 < prefix_sum[i - 1]:
                prefix_sum[i] = prefix_sum[i - 1] + 1
            else:
                prefix_sum[i] = 0
    suffix_sum = [0] * (1 + n)
    suffix_sum[n] = 1
    for i in range(n - 1, -1, -1):
        if text[i] == "l":
            suffix_sum[i] = suffix_sum[i + 1] + 1
        elif text[i] == "e":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "t":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "a":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "m":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "e":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "t":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "a":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "l":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "y":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "m":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "e":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "v":
            suffix_sum[i] = suffix_sum[i + 1]
        elif text[i] == "h":
            suffix_sum[i] = suffix_sum[i + 1]
    return sum(
        prefix_sum[i] * suffix_sum[i + 12]
        for i in range(n)
        if 0 < prefix_sum[i] and suffix_sum[i + 12] > 0
    )


text = input()
print(count_powerful_substrings(text))
