class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        curr = 1
        while(n >= curr):
            if n == curr:
                return True
            curr *= 3
        return False