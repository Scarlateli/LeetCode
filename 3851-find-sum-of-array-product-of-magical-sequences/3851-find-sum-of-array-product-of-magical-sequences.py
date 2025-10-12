from typing import List
MOD = 1_000_000_007

def mod_pow(a: int, e: int) -> int:
    res = 1
    a %= MOD
    while e:
        if e & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        e >>= 1
    return res

def popcount(x: int) -> int:
    return x.bit_count()  # Python 3.8+: bin(x).count('1') se preciso

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        # Pré-cálculos
        # 1) Combinações C(M, c) até M=m
        C = [[0]*(m+1) for _ in range(m+1)]
        for i in range(m+1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

        # 2) Tabela de potências nums[i]^c para c=0..m
        powtab = [[1]*(m+1) for _ in range(n)]
        for i in range(n):
            for c in range(1, m+1):
                powtab[i][c] = (powtab[i][c-1] * nums[i]) % MOD

        # dp[i][used][carry][ones] -> vamos manter camadas por i e por used
        # Para reduzir memória, usamos somente a linha atual e a próxima.
        # carry pode, no pior caso, atingir m (botando tudo num índice baixo).
        max_carry = m

        # dp é dict esparso: chave = (carry, ones) ; valor = soma
        # E manteremos uma lista de dicts por "used".
        from collections import defaultdict

        # Estado inicial: antes do índice 0, used=0, carry=0, ones=0 -> soma 1
        dp_used = [defaultdict(int) for _ in range(m+1)]
        dp_used[0][(0, 0)] = 1

        for i in range(n):
            new_dp_used = [defaultdict(int) for _ in range(m+1)]
            for used in range(m+1):
                if not dp_used[used]:
                    continue
                for (carry_in, ones_so_far), ways in dp_used[used].items():
                    # tentar escolher c repetições do índice i
                    max_c = m - used
                    # pequena poda: carry_in > max_c + (m - used - c) // 0? (opcional)
                    for c in range(0, max_c + 1):
                        # bit no nível i
                        s = c + carry_in
                        bit_i = s & 1
                        carry_out = s >> 1
                        if carry_out > max_carry:
                            # opcionalmente aumentar max_carry, mas m é limite prático
                            pass
                        used2 = used + c
                        if used2 > m:  # segurança
                            break
                        ones2 = ones_so_far + bit_i
                        if ones2 > k:  # poda por k
                            continue

                        # número de maneiras de posicionar essas c ocorrências agora
                        ways_choose = C[m - used][c]
                        # peso multiplicativo das c ocorrências deste índice
                        weight = powtab[i][c]

                        add = ways
                        add = (add * ways_choose) % MOD
                        add = (add * weight) % MOD

                        key = (carry_out, ones2)
                        new_dp_used[used2][key] = (new_dp_used[used2][key] + add) % MOD

            dp_used = new_dp_used  # próxima posição

        # Após processar todos os índices, ainda resta o carry.
        # Cada estado (carry, ones) contribui se used==m e ones + popcount(carry) == k
        ans = 0
        final_map = dp_used[m]
        for (carry, ones_so_far), ways in final_map.items():
            if ones_so_far > k:
                continue
            if ones_so_far + popcount(carry) == k:
                ans = (ans + ways) % MOD

        return ans % MOD
