class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1


# Example usage:
sol = Solution()

# Test cases
result1 = sol.isUgly(6)   # Output: True
result2 = sol.isUgly(1)   # Output: True
result3 = sol.isUgly(14)  # Output: False

print(result1)
print(result2)
print(result3)
