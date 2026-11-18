class Solution:
    def  addBinary(self, a: str, b: str) -> str:
        s: str = ""
        carry: int = 0
        i = len(a)-1
        j = len(b)-1
        while  i >=0 or  j >= 0 or  carry > 0:
            if i>=0 and a[i]=="1": carry+=1
            if j>=0 and b[j]=="1": carry+=1

            t: int = carry//2

            if 3 == carry:
                s = "1" + s
                carry = 1
            elif 2 == carry:
                s="0"+s
                carry=1
            elif 1 == carry:
                s="1"+s
                carry=0
            else:
                s="0"+s
            
            i -= 1
            j -= 1
        
        return s
        
