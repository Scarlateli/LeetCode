class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # Função auxiliar para verificar se um subarray é estritamente crescente
        def isStrictlyIncreasing(subarray):
            # Percorre o subarray comparando cada elemento com o próximo
            # Usamos len(subarray) - 1 para não ultrapassar o último índice
            for i in range(len(subarray) - 1):
                # Se o elemento atual for maior ou igual ao próximo,
                # não é estritamente crescente (precisa ser sempre menor)
                if subarray[i] >= subarray[i+1]:
                    return False
            # Se passou por todas as comparações sem problemas, é crescente!
            return True
        
        # Percorre todos os pares de subarrays adjacentes possíveis
        # len(nums) - 2*k + 1 garante que ambos os subarrays caibam no array
        # (primeiro subarray tem k elementos, segundo também tem k elementos)
        for i in range(len(nums) - 2*k + 1):
            # Extrai o primeiro subarray: começa em i, tem k elementos
            # slice [i:i+k] pega elementos dos índices i até i+k-1
            primeiro_subarray = nums[i:i+k]
            
            # Extrai o segundo subarray adjacente: começa em i+k, tem k elementos
            # slice [i+k:i+2*k] pega elementos dos índices i+k até i+2*k-1
            segundo_subarray = nums[i+k:i+2*k]
            
            # Verifica se AMBOS os subarrays são estritamente crescentes
            # Se sim, encontramos o par que o problema pede!
            if isStrictlyIncreasing(primeiro_subarray) and isStrictlyIncreasing(segundo_subarray):
                return True
        
        # Se o loop terminou sem encontrar nenhum par válido,
        # significa que não existem dois subarrays adjacentes crescentes
        return False     