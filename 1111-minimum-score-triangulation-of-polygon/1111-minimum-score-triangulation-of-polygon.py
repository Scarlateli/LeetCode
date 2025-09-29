class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                best = float('inf')
                for k in range(i + 1, j):
                    s = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    best = min(best, s)
                dp[i][j] = best
        return dp[0][n - 1]