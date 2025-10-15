class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Passo 1: Calcular quantos elementos crescentes TERMINAM em cada posição
        termina_em = [1] * n  # Inicializa com 1 (cada elemento sozinho)
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:  # Se é maior que o anterior
                termina_em[i] = termina_em[i-1] + 1  # Continua a sequência
            # Senão, já está como 1 (reinicia)
        
        # Passo 2: Calcular quantos elementos crescentes COMEÇAM em cada posição
        comeca_em = [1] * n  # Inicializa com 1
        
        for i in range(n - 2, -1, -1):  # Percorre de trás para frente
            if nums[i] < nums[i+1]:  # Se o próximo é maior
                comeca_em[i] = comeca_em[i+1] + 1  # Continua a sequência
            # Senão, já está como 1 (reinicia)
        
        # Passo 3: Encontrar o maior k possível
        max_k = 0
        
        # Verificar pares adjacentes em todas as posições
        for i in range(n - 1):
            # Na posição i termina uma sequência de tamanho termina_em[i]
            # Na posição i+1 começa uma sequência de tamanho comeca_em[i+1]
            # O maior k para esse par é o mínimo dos dois
            k_atual = min(termina_em[i], comeca_em[i+1])
            max_k = max(max_k, k_atual)
        
        # Passo 4: Verificar sequências individuais divididas ao meio
        # Uma sequência longa pode ser dividida em dois subarrays iguais
        for i in range(n):
            # Se temos uma sequência crescente de tamanho X,
            # podemos dividi-la em dois subarrays de tamanho X//2
            k_dividido = termina_em[i] // 2
            max_k = max(max_k, k_dividido)
        
        return max_k