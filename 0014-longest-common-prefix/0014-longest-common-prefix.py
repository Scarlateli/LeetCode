class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return "" #se o array estiver vazia, nao traz nenhum prefixo, string vazia

        strs.sort() #ordenacao, como um dicionario

        p1 = strs [0] #menor indice
        p2 = strs [-1] #maior indice

        i = 0 #indice para percorrer caractere por caractere

        while i < len(p1) and i < len(p2) and p1[i] == p2[i]: #enquanto nao estourar o tamanho de nenhuma das duas e se a posicao for igual, avanca, se nao, para.
            i += 1

        return p1[:i] #slicing, pega do inicio da string ate o final, os primeiros "i" caracteres

        



        

