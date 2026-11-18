class Solution:
    def  maxArea(self, height: List[int]) -> int:
        maximum = start=0
        end=len(height)-1
        diff = len(height) - 1
    
        while  start <end:
            h = height[end] if height[start] > height[end] else height[start]
            # Calculate area
            calc = h*diff
            if  calc > maximum:
                maximum=calc
            # Gets one closer each time
            diff -=1

            # Move index
            if  not height[start] >= height[end]:
                start+=1
            else:
                end-=1

        return  maximum
