class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # its another hashtable problem
        # we will go through both strings but start with one first
        # store its letters in a dictionary, then go through the other string
        # then using the stored letters to construct the second string
        # if not possible return False
        # check if the dictionary is empty, if yes, return True, otherwise False
        # Time: O(n), space: O(n)
        letter_bank = dict()
        for letter in s:
            if letter not in letter_bank:
                letter_bank[letter] = 1
            else:
                letter_bank[letter] += 1
        for letter in t:
            print(letter)
            if letter not in letter_bank:
                return False
            else:
                letter_bank[letter] -= 1
                if letter_bank[letter] == 0:
                    del letter_bank[letter]
        print(letter_bank)
        return not letter_bank
