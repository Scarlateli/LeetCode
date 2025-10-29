class Solution:
    def smallestNumber(self, n: int) -> int:
        bits = n.bit_length()
        return (1 << bits) - 1

        