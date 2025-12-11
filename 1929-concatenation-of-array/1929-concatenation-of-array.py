#primeiro problema de array do leetcode quest
#create array ans
#lenght 2n
# ans[i] == nums[i]
# ans[i + n] == nums[i] for 0 <= i < n

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
        