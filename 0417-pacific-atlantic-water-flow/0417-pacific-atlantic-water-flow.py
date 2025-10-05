class Solution:
    def pacificAtlantic(self, a):
        n, m = len(a), len(a[0])
        ans = [[[False, False] for _ in range(m)] for _ in range(n)]
        dir = [(0,1),(0,-1),(1,0),(-1,0)]

        #  DFS helper
        def dfs(x, y, ocean):
            #  Did the ocean reach this cell?
            if (ocean == 'p' and ans[x][y][0]) or (ocean != 'p' and ans[x][y][1]):
                return
            if ocean == 'p': ans[x][y][0] = True
            else: ans[x][y][1] = True

            #  Move 4 directions
            for dx, dy in dir:
                cx, cy = x + dx, y + dy
                if 0 <= cx < n and 0 <= cy < m and a[cx][cy] >= a[x][y]:
                    #  Flow upwards
                    dfs(cx, cy, ocean)

        #  Start from top (pacific)
        for i in range(m): dfs(0, i, 'p')
        #  Start from left (pacific)
        for i in range(n): dfs(i, 0, 'p')
        #  Start from down (atlantic)
        for i in range(m): dfs(n - 1, i, 'a')
        #  Start from right (atlantic)
        for i in range(n): dfs(i, m - 1, 'a')

        realans = []
        for i in range(n):
            for j in range(m):
                if ans[i][j][0] and ans[i][j][1]:
                    realans.append([i, j])
        return realans