from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        restos = Counter(num % value for num in nums)
        
        # Encontra o resto que aparece menos vezes
        min_count = min(restos.get(i, 0) for i in range(value))
        
        # Depois das rodadas completas, qual resto falta?
        for i in range(value):
            if restos.get(i, 0) == min_count:
                return min_count * value + i