class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count = Counter(nums)                   # solution 1: line sweep, TC = O(nlogn)
        presum = defaultdict(int)
        for x in count:                 # line sweep
            presum[x-k] += count[x]
            presum[x+k+1] -= count[x]
        keys = sorted(presum.keys() | count.keys())     # search all possible keys
        ans, total = 0, 0
        for x in keys:
            total += presum[x]                          # maximum frequency for x
            ops = min(total-count[x], numOperations)    # number of operations bounded by numOperations
            ans = max(ans, count[x] + ops)              # update ans
        return ans