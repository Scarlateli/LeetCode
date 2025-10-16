from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        restos = Counter(num % value for num in nums)
        
        mex = 0
        while mex < len(nums):
            if restos[mex % value] > 0:
                restos[mex % value] -= 1
                mex += 1
            else:
                break
        
        return mex