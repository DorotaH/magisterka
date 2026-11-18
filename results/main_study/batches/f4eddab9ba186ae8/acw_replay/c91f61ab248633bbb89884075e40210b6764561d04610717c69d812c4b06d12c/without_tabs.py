import math


class Solution:

    def adjustLastLine(self, words_line, maxWidth):
        return ' '.join(words_line).ljust(maxWidth, ' ')

    def adjustLine(self, words_line, count_characters, maxWidth):
        word_count = len(words_line)

        ##unique case where the count characters same width line and count words is one
        if word_count == 1 and count_characters - 1 == maxWidth:
            return ''.join(words_line)

        sp  = maxWidth - (count_characters - 1)

        if 1 >= word_count:
            return words_line[0] + sp * " "
        wr  = 0 if 2 > word_count else math.ceil(sp / (word_count - 1))
        for sub_i in range(word_count - 1):
            if sp > 0:
                wr  = math.ceil(sp / (word_count - sub_i - 1))
                words_line[sub_i] += " " + (wr * " ")
                sp -= wr
            else:
                words_line[sub_i] += " "
        return ''.join(words_line)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res_p = []
        gt    = []
        s     = 0
        i     = 0
        while i < len(words):
            res = len(words[i]) + 1
            if res + s - 1 > maxWidth:
                res_p += self.adjustLine(gt, s, maxWidth),
                gt = []
                s  = 0
            elif i == len(words) - 1:
                gt += words[i],
                res_p += self.adjustLastLine(gt, maxWidth),
                gt = []
                s  = 0
                i += 1
            else:
                gt += words[i],
                s  += res
                i  += 1
        return res_p
