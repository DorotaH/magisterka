class Solution:
    def isHappy(self, n: int) -> bool:
        k = n
        store = [k]
        while True:
            store.append(k)
            string = str(k)

            sum_squares = sum(int(s)**2 for s in string)
            k = sum_squares

            if(k==1):
                return True
            if(k in store):
                return False


