class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []

        s_list = list(s)

        #coleta todas as vogais
        for i in s_list:
            if i in "AEIOUaeiou":
                vowels.append(i)

        if vowels == []:
            return s

        # sort the vowels
        vowels.sort()

        count = 0

        #substituir as vogais originais pelas sorteadas

        for j in range(len(s)):
            if s_list[j] in "AEIOUaeiou":
                s_list[j]= vowels[count]
                count += 1

        return "".join(s_list)                    
        