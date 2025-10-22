
# #  using Dijkstra Algorithm

from collections import defaultdict

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dijkstra(src):
            dist = [float('inf')] * n
            visited = [False] * n
            dist[src] = 0

            for _ in range(n):
                
                u = -1
                min_dist = float('inf')
                for i in range(n):
                    if not visited[i] and dist[i] < min_dist:
                        min_dist = dist[i]
                        u = i

                if u == -1:
                    break  

                visited[u] = True

                
                for v, w in adj[u]:
                    if not visited[v] and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            
            return sum(1 for i in range(n) if i != src and dist[i] <= distanceThreshold)

       
        min_count = n
        result = -1

        for i in range(n):
            count = dijkstra(i)
            if count <= min_count:
                min_count = count
                result = i  
        return result


# Using Floyd-Warshall Algorithm


# class Solution(object):
#     def findTheCity(self, n, edges, distanceThreshold):
        
#         dist = [[float('inf')] * n for _ in range(n)]

#         for i in range(n):
#             dist[i][i] = 0

#         for u, v, w in edges:
#             dist[u][v] = w
#             dist[v][u] = w

#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     if dist[i][k] + dist[k][j] < dist[i][j]:
#                         dist[i][j] = dist[i][k] + dist[k][j]
                        
#         min_count = n
#         result = -1

#         for i in range(n):
#             count = 0
#             for j in range(n):
#                 if i != j and dist[i][j] <= distanceThreshold:
#                     count += 1

#             if count <= min_count:
#                 min_count = count
#                 result = i

#         return result




solution = Solution()
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
threshold = 4
print(solution.findTheCity(n, edges, threshold)) 