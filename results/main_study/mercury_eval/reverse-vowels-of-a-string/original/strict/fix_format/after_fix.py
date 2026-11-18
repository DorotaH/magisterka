class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1:
            return s[0]

        VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} #Set is used as it has a better search TC than List
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in VOWELS:
                left += 1

            if s[right] not in VOWELS:
                right -= 1

            if s[left] in VOWELS and s[right] in VOWELS:
                tmp = s[left]
                s[left] = s[right]
                s[right] = tmp
                left += 1
                right -= 1

        return "".join(s)
