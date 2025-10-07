class Solution:
    def avoidFlood(self, rain: List[int]) -> List[int]:
        n = len(rain)
        uf = UnionFind(n + 1)
        map_lake = {}
        res = [1] * n

        for i, lake in enumerate(rain):
            if lake != 0:
                res[i] = -1
                uf.unite(i)
                
                if lake in map_lake:
                    prev = map_lake[lake]
                    dry = uf.find(prev + 1)
                    
                    if dry >= i:
                        return []

                    res[dry] = lake
                    uf.unite(dry)
                    map_lake[lake] = i
                else:
                    map_lake[lake] = i

        return res


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size + 1))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i: int):
        self.parent[i] = self.find(i + 1)