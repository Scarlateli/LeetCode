from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1
        while True:
            s = str(i)
            
            if '0' in s:
                i += 1
                continue
            
            c = Counter(s)
            
            if all(int(k) == v for k, v in c.items()):
                return i
            
            i += 1