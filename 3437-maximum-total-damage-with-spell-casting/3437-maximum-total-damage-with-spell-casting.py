class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)                       # valores distintos
        n = len(keys)
        gain = [freq[k] * k for k in keys]        # ganho de pegar cada valor

        dp = [0] * n
        dp[0] = gain[0]

        j = -1  # último índice compatível com i (keys[j] <= keys[i]-3)
        for i in range(1, n):
            # avança j até o último que ainda é compatível com keys[i]
            while j + 1 < i and keys[j + 1] <= keys[i] - 3:
                j += 1

            take = gain[i] + (dp[j] if j >= 0 else 0)
            dp[i] = max(dp[i - 1], take)

        return dp[-1]