class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)     # dp[i] = novos que aprenderam no dia i
        dp[1] = 1

        to_share = 0           # pessoas ativas para compartilhar no dia atual

        for day in range(2, n + 1):
            # Quem passa a compartilhar hoje (aprendeu em day - delay)
            start = day - delay
            if start >= 1:
                to_share = (to_share + dp[start]) % MOD

            # Quem esquece hoje (aprendeu em day - forget)
            stop = day - forget
            if stop >= 1:
                to_share = (to_share - dp[stop]) % MOD  # tira da janela

            # Todos os que podem compartilhar hoje geram novos aprendizados
            dp[day] = to_share

        # Somar quem ainda sabe no fim do dia n: os que aprenderam
        # depois de n - forget (não deu tempo de esquecer)
        left = max(1, n - forget + 1)
        return sum(dp[left: n + 1]) % MOD
