class Solution:
    def  addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1="0"*(len(num2)-len(num1))+num1
        elif len(num1)>len(num2):
            num2 = "0"*(len(num1)-len(num2)) + num2


        res=""
        carry=False
        for  i in  range(len(num1)-1, -1,-1):
            digit=(int(num1[i])+int(num2[i])+carry)
            res=str(digit%10)+res
            carry=digit>9
        if carry:
            res="1"+res
        return res
