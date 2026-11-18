class  Solution:
    def  isHappy(self, n: int) -> bool:
        k = n
        store = [k]
        while(True):
            store.append(k)
            string = str(k)

            sum_squares = 0
            for  s in  string:
                sum_squares += int(s)**2
            k = sum_squares
            
            if(1==k):
                return True
            if(k in store):
                return False


        