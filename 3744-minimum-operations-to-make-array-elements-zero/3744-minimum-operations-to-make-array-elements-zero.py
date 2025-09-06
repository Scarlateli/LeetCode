from typing import List

class Solution:
    # aqui eu calculo F(num) = soma de steps(x) para x = 1..num
    # steps(x) é quantas vezes eu preciso dividir x por 4 (floor(x/4)) até virar 0
    # obs: steps(x) = ⌊log4(x)⌋ + 1 = ceil(bit_length(x)/2), e steps(0) = 0
    def get(self, num: int) -> int:
        # se o num for 0 ou negativo, não tem nada pra somar
        if num <= 0:
            return 0

        i = 1        # i é o nível do bloco em potências de 2 (bit-length)
                     # i=1 cobre [1..1], i=2 cobre [2..3], i=3 cobre [4..7], i=4 cobre [8..15]...
        base = 1     # base é o começo do bloco atual = 2^(i-1)
        cnt = 0      # cnt acumula o prefixo F(num)

        # enquanto ainda tiver parte do bloco dentro de [1..num]
        while base <= num:
            # o fim do bloco seria 2*base - 1, mas eu corto no num se passar
            right = min(base * 2 - 1, num)

            # quantidade de números desse bloco que realmente caem em [1..num]
            length = right - base + 1

            # todos os números desse bloco têm o mesmo steps(x)
            # o steps é ceil(i/2), que eu escrevo como (i+1)//2
            weight = (i + 1) // 2

            # somo a contribuição desse bloco ao prefixo
            cnt += weight * length

            # avanço pro próximo bloco
            i += 1
            base *= 2

        return cnt

    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for l, r in queries:
            # S é a soma de steps(x) para x em [l..r]
            # eu uso o prefixo: F(r) - F(l-1)
            S = self.get(r) - self.get(l - 1)

            # cada operação consome 2 steps de uma vez
            # então o mínimo de operações é ceil(S/2)
            # faço isso como (S+1)//2 pra trabalhar só com inteiros
            res += (S + 1) // 2
        return res
