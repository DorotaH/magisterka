class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        self.res = ""
        def process(cur: str, place: int):
            zeroes = 3 - len(cur)
            for i in range(zeroes): cur = "0" + cur
            string = self.segment(cur[0], cur[1], cur[2], place)
            if string:
                if place > 0: self.res = string + " " + self.res
                else: self.res = string

        str_val = str(num)[::-1]
        for i in range(ceil(len(str_val) / 3)):
            process(str_val[i*3:i*3+3][::-1], i)

        return self.res[:-1]

    def segment(self, h, t, o, place) -> str:
        under_ten = {"0":"", "1": "One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}
        ten_to_nineteen = {"10":"Ten", "11":"Eleven", "12":"Twelve", "13":"Thirteen", "14":"Fourteen", "15":"Fifteen", "16":"Sixteen", "17":"Seventeen", "18":"Eighteen", "19":"Nineteen"}
        tens = {"0":"", "2":"Twenty", "3":"Thirty", "4":"Forty", "5":"Fifty", "6":"Sixty", "7":"Seventy", "8":"Eighty", "9":"Ninety"}
        higher = {0:"", 1:"Thousand", 2:"Million", 3:"Billion"}

        res = []
        if h != "0":
            res.append(under_ten[h])
            res.append("Hundred")
        if t == "1":
            res.append(ten_to_nineteen[t + o])
        else:
            res.append(tens[t])
            res.append(under_ten[o])
        res = [i for i in res if i]
        if res: res.append(higher[place])
        return " ".join(res)
