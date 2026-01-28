class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len (nums)
        count = [0] * (n+1)

        for num in nums:
            count[num] += 1

        duplicado = 0
        faltando = 0

        for i in range (1, n + 1):
            if count[i] == 2:
                duplicado = i
            if count [i] == 0:
                faltando = i    
        

        return [duplicado,faltando]