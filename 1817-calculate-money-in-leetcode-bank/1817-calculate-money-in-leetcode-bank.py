arr = [1]
for i in range(1, 1001):
    if i%7 == 0: curr = arr[-7] + 1
    else: curr = arr[-1] + 1
    arr.append(curr)

class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(arr[:n])
        
                