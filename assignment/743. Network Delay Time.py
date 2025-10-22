from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))  

        def dijkstra(src):
            dist = [float('inf')] * (n + 1)
            visited = [False] * (n + 1)
            dist[src] = 0

            for _ in range(n):
                
                u = -1
                min_dist = float('inf')
                for i in range(1, n + 1):
                    if not visited[i] and dist[i] < min_dist:
                        min_dist = dist[i]
                        u = i

                if u == -1:
                    break 

                visited[u] = True

                for v, w in adj[u]:
                    if not visited[v] and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            max_dist = max(dist[1:])  
            return -1 if max_dist == float('inf') else max_dist

        return dijkstra(k)

solution = Solution()
print(solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  
