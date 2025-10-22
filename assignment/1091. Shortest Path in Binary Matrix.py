from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),
                      (0, 1),(1, -1), (1, 0), (1, 1) ]

        queue = deque()
        queue.append((0, 0, 1))  # (x, y, steps)

        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True

        while queue:
            x, y, steps = queue.popleft()

            if x == n - 1 and y == n - 1:
                return steps 

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))

        return -1 
    
sol = Solution()
print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))  

print(sol.shortestPathBinaryMatrix([[0,0,0],
                                    [1,1,0],
                                    [1,1,0]]))  

