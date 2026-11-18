class  Solution:
    def largestRectangleArea(self, a: List[int]) -> int:
        a=[0]+a+[0]
        n = len(a)
        stack = [0]
        ret=0
        for  i in  range(1, n):
            while  a[stack[-1]] > a[i]:
                idx=stack.pop()
                this_ret=(i-stack[-1]-1)*a[idx]
                ret=max(ret, this_ret)
            if stack and a[stack[-1]] == a[i]:
                stack.pop()
            stack.append(i)
        return ret


        