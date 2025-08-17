class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Casos de borda
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        window = 1.0   # soma das probabilidades que podem gerar o próximo i (estados < k)
        ans = 0.0

        for i in range(1, n + 1):
            dp[i] = window / maxPts

            if i < k:
                window += dp[i]  # ainda pode sortear
            else:
                ans += dp[i]     # estado terminal

            if i - maxPts >= 0 and i - maxPts < k:
                window -= dp[i - maxPts]

        return ans
