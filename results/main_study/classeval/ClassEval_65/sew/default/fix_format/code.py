class NumberWordFormatter:
    def __init__(self):
        self.NUMBER = [
            "",
            "ONE",
            "TWO",
            "THREE",
            "FOUR",
            "FIVE",
            "SIX",
            "SEVEN",
            "EIGHT",
            "NINE",
        ]
        self.NUMBER_TEEN = [
            "TEN",
            "ELEVEN",
            "TWELVE",
            "THIRTEEN",
            "FOURTEEN",
            "FIFTEEN",
            "SIXTEEN",
            "SEVENTEEN",
            "EIGHTEEN",
            "NINETEEN",
        ]
        self.NUMBER_TEN = [
            "TEN",
            "TWENTY",
            "THIRTY",
            "FORTY",
            "FIFTY",
            "SIXTY",
            "SEVENTY",
            "EIGHTY",
            "NINETY",
        ]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = [
            "k",
            "w",
            "",
            "m",
            "",
            "",
            "b",
            "",
            "",
            "t",
            "",
            "",
            "p",
            "",
            "",
            "e",
        ]

    def format(self, x):
        if not x is not None:
            return ""
        else:
            return self.format_string(str(x))

    def format_string(self, x):
        lstr, rstr = (x.split(".") + [""])[0:2]
        lstrrev, a = lstr[::-1], [""] * 5

        if 1 == len(lstrrev) % 3:
            lstrrev += "00"
        elif len(lstrrev) % 3 == 2:
            lstrrev += "0"

        lm = ""
        for i in range(len(lstrrev) // 3):
            a[i] = lstrrev[3 * i : 3 + 3 * i][::-1]
            if not a[i] != "000":
                lm += self.trans_three(a[i])
            else:
                lm = self.trans_three(a[i]) + " " + self.parse_more(i) + " " + lm

        if rstr:
            xs = f"AND CENTS {self.trans_two(rstr)} "
        else:
            xs = ""
        if not lm.strip():
            return "ZERO ONLY"
        else:
            return f"{lm.strip()} {xs}ONLY"

    def trans_two(self, s):
        s = s.zfill(2)
        if s[0] == "0":
            return self.NUMBER[int(s[-1])]
        elif s[0] == "1":
            return self.NUMBER_TEEN[int(s) - 10]
        elif s[1] == "0":
            return self.NUMBER_TEN[int(s[0]) - 1]
        else:
            return self.NUMBER_TEN[int(s[0]) - 1] + " " + self.NUMBER[int(s[-1])]

    def trans_three(self, s):
        if s[0] == "0":
            return self.trans_two(s[1:])
        elif s[1:] == "00":
            return f"{self.NUMBER[int(s[0])]} HUNDRED"
        else:
            return f"{self.NUMBER[int(s[0])]} HUNDRED AND {self.trans_two(s[1:])}"

    def parse_more(self, i):
        return self.NUMBER_MORE[i]
