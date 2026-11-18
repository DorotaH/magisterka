class Solution:
    def intToRoman(self, num: int) -> str:
        hmap = {
            1:    'I',
            4:    'IV',
            5:    'V',
            9:    'IX',
            10:    'X',
            40:    'XL',
            50:    'L',
            90:    'XC',
            100:    'C',
            400:    'CD',
            500:    'D',
            900:    'CM',
            1000:    'M'
        }
        s = ''
        xlist = list(hmap.keys())
        x = xlist[-1]
        while num != 0:
            if num >= x:
                s += hmap.get(x, '') * (num // x)
                num -= x * (num // x)
            else:
                x = xlist[xlist.index(x) - 1]
                print(x)
        return s
