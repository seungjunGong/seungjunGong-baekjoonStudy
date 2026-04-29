class Solution:
    def kthCharacter(self, k: int) -> str:
        shift = 0
        length = 1

        while length < k:
            length *= 2

        while k > 1:
            half = length // 2

            if k > half:
                k -= half
                shift += 1

            length = half    
        return chr(ord('a') + shift % 26)