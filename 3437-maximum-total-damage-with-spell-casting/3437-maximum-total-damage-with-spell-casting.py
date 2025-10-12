class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # 1) conte as frequências e ordene os danos distintos
        freq = Counter(power)
        keys = sorted(freq)
        n = len(keys)

        # 2) dp[i] = melhor total usando apenas keys[0..i]
        dp = [0] * n
        dp[0] = freq[keys[0]] * keys[0]

        # 3) para cada dano distinto a partir do segundo
        for i in range(1, n):
            # valor se eu "pegar" esse dano (uso todos os feitiços desse valor)
            take = freq[keys[i]] * keys[i]

            # 4) achar via busca binária o último índice ans que não conflita
            #    (keys[ans] <= keys[i] - 3)
            l, r, ans = 0, i - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if keys[mid] <= keys[i] - 3:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1

            # se existe um compatível atrás, some o melhor até ele
            if ans >= 0:
                take += dp[ans]

            # 5) melhor entre não pegar o atual ou pegar e somar compatível
            dp[i] = max(dp[i - 1], take)

        # 6) resposta final
        return dp[-1]