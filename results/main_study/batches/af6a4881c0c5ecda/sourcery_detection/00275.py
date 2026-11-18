class Solution:
    def isIsomorphic(self, s, t):
        map1 = {}
        map2 = {}

        for char_s, char_t in zip(s, t):
            if char_s in map1:
                if map1[char_s] != char_t:
                    return False
            else:
                map1[char_s] = char_t

            if char_t in map2:
                if map2[char_t] != char_s:
                    return False
            else:
                map2[char_t] = char_s

        return True
