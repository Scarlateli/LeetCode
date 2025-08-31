MX = 10**5 + 1
divisors = [[] for _ in range(MX)]
for x in range(1, MX):
    for y in range(x, MX, x):
        divisors[y].append(x)


class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        def split(n, k):
            if k == 1:
                yield n,
            elif k == 2:
                for d in divisors[n]:
                    yield d, n // d
            else:
                for d, e in split(n, 2):
                    for left in split(d, k // 2):
                        for right in split(e, k - k // 2):
                            yield left + right

        best = inf
        for choice in split(n, k):
            d = max(choice) - min(choice)
            if d < best:
                best = d
                ans = sorted(choice)
        return ans