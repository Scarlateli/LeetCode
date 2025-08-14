class Solution(object):
    def largestGoodInteger(self, num):
        best = ""
        for i in range(len(num) - 2):
            s = num[i:i+3]
            if s[0] == s[1] == s[2]:
                if best == "" or s > best:
                    best = s
        return best
        