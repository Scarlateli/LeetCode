from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # Soma, para x = 1..n, do número de vezes que precisamos aplicar x <- floor(x/4) até virar 0
        # (equivale ao número de dígitos de x em base 4)
        def prefix(n: int) -> int:
            if n <= 0:
                return 0
            total = 0
            pow4 = 1     # 4^(k-1) para o bloco de k dígitos
            k = 1        # "custo" por número nesse bloco (nº de dígitos em base 4)
            
            # Somar blocos completos: [4^(k-1), 4^k - 1]
            while pow4 * 4 <= n:
                count = 3 * pow4           # quantidade de números com k dígitos em base 4
                total += k * count
                pow4 *= 4
                k += 1
            
            # Pedaço final (incompleto) do último bloco: [pow4, n]
            total += k * (n - pow4 + 1)
            return total

        ans = 0
        for l, r in queries:
            S = prefix(r) - prefix(l - 1)
            ans += (S + 1) // 2  # ceil(S/2)
        return ans
