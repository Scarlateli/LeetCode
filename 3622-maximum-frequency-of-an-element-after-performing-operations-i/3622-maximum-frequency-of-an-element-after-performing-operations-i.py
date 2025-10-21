class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        fm = defaultdict(int)
        for x in nums:
            fm[x] += 1
        
        def get_freq(target):
            l = bisect_left(nums, target - k)
            r = bisect_right(nums, target + k)
            ops = r - l - fm[target]
            return fm[target] + min(ops, numOperations)
        
        res = 0
        for n in range(nums[0], nums[-1] + 1):
            res = max(res, get_freq(n))
        
        return res