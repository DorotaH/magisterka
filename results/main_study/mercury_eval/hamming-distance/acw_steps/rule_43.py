__NOVEL__ = True

class Solution:
    def built_in_hamming_distance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
    
    def custom_hamming_distance(self, x: int, y: int) -> int:
        def count_bits(n):
            count = 0

            while 0 < n:
                n = (n & (n - 1))
                count += 1
            
            return count
        
        return count_bits(x ^ y)

    def hammingDistance(self, x: int, y: int) -> int:
        if __NOVEL__:
            return self.custom_hamming_distance(x, y)
        return self.built_in_hamming_distance(x, y)
