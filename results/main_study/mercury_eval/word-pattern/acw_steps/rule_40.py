class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        if len(words) != len(pattern):
            return False
        mapping_pat_word = dict()
        mapped_word_pat = set()
        for pat, word in zip(pattern, words):
            if pat in mapping_pat_word:
                if mapping_pat_word[pat] != word:
                    return False
            else:
                if word in mapped_word_pat:
                    return False
                mapping_pat_word[pat] = word
                mapped_word_pat.add(word)
        return True