class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        # Inicialização das variáveis em uma linha (múltipla atribuição)
        # n = tamanho total do array
        # Len = tamanho da sequência crescente ATUAL (começa com 1)
        # prev = tamanho da sequência crescente ANTERIOR (começa com 0 pois não existe anterior ainda)
        # k = maior k encontrado até agora, nossa resposta (começa com 0)
        n, Len, prev, k = len(nums), 1, 0, 0
        
        # Percorre o array a partir do segundo elemento (índice 1)
        for i in range(1, n):
            
            # Verifica se o elemento atual é maior que o anterior
            # Se sim, a sequência crescente continua
            if nums[i] > nums[i-1]:
                Len += 1  # Aumenta o tamanho da sequência atual
            
            # Se não for maior, a sequência crescente quebrou/terminou
            else:
                # Quando uma sequência termina, calculamos o melhor k possível
                # usando três estratégias diferentes:
                
                # Estratégia 1: k atual (o melhor que já encontramos antes)
                # Estratégia 2: Len//2 (dividir a sequência atual ao meio)
                #   - Exemplo: se Len=6 ([1,2,3,4,5,6]), podemos fazer k=3
                #   - Primeiro subarray: [1,2,3], Segundo: [4,5,6]
                # Estratégia 3: min(Len, prev) (usar sequência anterior + atual como par adjacente)
                #   - Se prev=4 e Len=5, podemos pegar k=4
                #   - Pega 4 elementos do final da sequência anterior
                #   - Pega 4 elementos do início da sequência atual
                #   - Eles são adjacentes!
                k = max(k, Len//2, min(Len, prev))
                
                # Agora que a sequência atual terminou:
                prev = Len  # Ela se torna a sequência "anterior"
                Len = 1     # Reinicia o contador para a próxima sequência
                            # (começa com 1 porque o elemento atual já conta)
        
        # Quando o loop termina, ainda temos a ÚLTIMA sequência que não foi processada
        # (porque ela só é processada quando "quebra", e no final do array não quebra)
        # Então fazemos o mesmo cálculo mais uma vez com a última sequência
        return max(k, Len//2, min(Len, prev))