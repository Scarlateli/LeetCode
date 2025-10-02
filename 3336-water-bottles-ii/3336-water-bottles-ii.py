class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles     # começa com as cheias recebidas
        emptyBottles = 0
        totalDrank = 0
        exchangeRate = numExchange   # taxa inicial de troca

        while fullBottles > 0:
            # beber todas as garrafas cheias
            totalDrank += fullBottles
            emptyBottles += fullBottles
            fullBottles = 0

            # trocar se tiver garrafas vazias suficientes
            if emptyBottles >= exchangeRate:
                fullBottles += 1          # ganha 1 garrafa cheia
                emptyBottles -= exchangeRate
                exchangeRate += 1         # taxa aumenta
            else:
                break

        return totalDrank
