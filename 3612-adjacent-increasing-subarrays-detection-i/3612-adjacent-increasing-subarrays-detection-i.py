# array chamada nums
# integer k
# determinar se existem duas subarrys adjacentes com tamanho (lenght) k 
# as duas subarrays estao crescendo
# checar se existem duas subarrys começando com indice a e b, onde (a < b)
# as duas subarrays nums[a..a + k - 1] e nums[b..b + k - 1] estao crescendo
# elas sao adjacentes, entao b = a + k
#retornar true se for possivel achar as duas subarryays, falso se nao for.

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        knew = k - 1
        if knew == 0:
            return True
        for j in range(k + 1, len(nums)):
            if nums[j] > nums[j - 1] and nums[j - k] > nums[j - k - 1]:
                knew -= 1
            else:
                knew = k - 1
            if knew == 0:
                return True
        return False