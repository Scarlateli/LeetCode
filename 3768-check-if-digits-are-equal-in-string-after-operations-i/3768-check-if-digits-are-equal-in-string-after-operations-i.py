class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            arr = []
            for i in range(1, len(s)):
                curr = (int(s[i - 1]) + int(s[i])) % 10
                arr.append(str(curr))
            s = "".join(arr)

        return s[0] == s[1]        