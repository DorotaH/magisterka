class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # # Approach #1 : Time Limit Exceeded
        # def is_palindrome(words):
        #     return words == words[::-1]

        # output = []
        # for i, word1 in enumerate(words):
        #     for j, word2 in enumerate(words):
        #         if i == j:
        #             continue
        #         if is_palindrome(word1 + word2):
        #             output.append([i, j])

        # return output

        # Approach #2
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]

    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[: len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word):
        result = []
        node = self.root

        while word:
            if node.word_id >= 0 and self.is_palindrome(word):
                result.append([index, node.word_id])
            if word[0] not in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        result.extend(
            [index, palindrome_word_id]
            for palindrome_word_id in node.palindrome_word_ids
        )
        return result

