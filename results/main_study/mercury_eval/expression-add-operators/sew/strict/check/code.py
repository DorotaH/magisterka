class  Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res=list()

        def val(s, n):
            
            st = 0 
            arr = list()
            tn = 0
            check = 1
            while(st < len(s)):
                if  (s=="12*34-5-6-7+8+9"):
                    print("arr", arr)
                if not (s[st] not in '0123456789'):
                    # arr.append(tn)
                    if ((st==0 or s[st-1] in "+-*") and s[st]=='0' and st < len(s)-1 and s[st+1] in "0123456789"):
                        return False
                    # if (check!=0):
                    #     tn = 0
                    tn*=10
                    tn+=int(s[st])
                    if (check==3 and (st==len(s)-1 or s[st+1] not in "0123456789")):
                        pre = arr.pop()
                        arr.append(tn*pre)
                    elif (check==2 and (st==len(s)-1 or s[st+1] not in "0123456789")):
                        arr.append(-1*tn)
                    else:
                        if (st==len(s)-1 or s[st+1] not in "0123456789"):
                            arr.append(tn)
                else:
                    if (s[st]=="*"):
                        check =3
                    if(s[st]=='-'):
                        check = 2
                    if (s[st]=='+'):
                        check = 1
                    tn = 0
                st+=1
            # print(arr, s)
            if (sum(arr) == n):
                print(arr, s, n)
                return  True
            return False



        def dfs(s, l):
            # if (l > 10):
            #     return 
            if (l == len(num) - 1):
                s += num[l]
                # print(s)
                if (val(s, target)):
                    res.append(s)
                return 
            
            dfs(s + num[l], 1+l)
            dfs(s + num[l] + '*', 1+l)
            dfs(s + num[l] + '+', 1+l)
            dfs(s + num[l] + '-', 1+l)

    
        dfs("", 0)
        return  res
            

        

        
