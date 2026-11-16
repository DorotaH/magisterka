def count_char_position(str1):
    return sum(
        i in [ord(str1[i]) - ord("A"), ord(str1[i]) - ord("a")]
        for i in range(len(str1))
    )
