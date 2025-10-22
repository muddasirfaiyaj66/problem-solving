from collections import deque

class Solution(object):
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])

        if k >= m + n - 2:
            return m + n - 2

        visited = [[-1 for _ in range(n)] for _ in range(m)]
        visited[0][0] = k
        queue = deque()
        queue.append((0, 0, 0, k))
        
        while queue:
            x, y, steps, remaining_k = queue.popleft()
            if x == m - 1 and y == n - 1:
                return steps

            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    nk = remaining_k - grid[nx][ny]  

                    if nk >= 0 and (visited[nx][ny] == -1 or nk > visited[nx][ny]):
                        visited[nx][ny] = nk
                        queue.append((nx, ny, steps + 1, nk))
        
        return -1

solution = Solution()
grid = [[0,1,1],[1,1,0],[1,1,0]]
k = 1
print(solution.shortestPath(grid, k))  