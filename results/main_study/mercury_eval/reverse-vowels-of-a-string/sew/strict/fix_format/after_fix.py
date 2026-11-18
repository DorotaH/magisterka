class  Solution:
    def reverseVowels(self, s: str) -> str:
        if  len(s) == 1:
            return  s[0]

        VOWELS={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} #Set is used as it has a better search TC than List
        s=list(s)
        left = 0
        right = len(s) - 1

        while  right > left:
            if s[left] not in VOWELS:
                left = left + 1

            if s[right] not in VOWELS:
                right = right - 1

            if s[left] in VOWELS and s[right] in VOWELS:
                tmp=s[left]
                s[left]=s[right]
                s[right]=tmp
                left = left + 1
                right = right - 1

        return  "".join(s)
