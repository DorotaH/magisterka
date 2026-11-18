class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        st = set()
        max_len = 1
        low = 0
        high = 1
        st.add(s[low])
        while low < n - 1 and high < n:
            print("checking ", low, " and ", high)
            if s[high] not in st:
                st.add(s[high])
                high += 1
                length = high - low
                max_len = max(max_len, length)
            else:
                low += 1
                st.remove(s[low - 1])
        return max_len
