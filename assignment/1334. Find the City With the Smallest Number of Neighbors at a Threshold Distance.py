
# #  using Dijkstra Algorithm

# import heapq
# from collections import defaultdict

# class Solution(object):
#     def findTheCity(self, n, edges, distanceThreshold):
#         adj = defaultdict(list)
#         for v1, v2, dist in edges:
#             adj[v1].append((v2, dist))
#             adj[v2].append((v1, dist))
        
#         def dijkstra(src):
#             heap = [(0, src)]
#             dist = [float('inf')] * n
#             dist[src] = 0

#             while heap:
#                 cur_dist, node = heapq.heappop(heap)
#                 for nei, w in adj[node]:
#                     if dist[nei] > cur_dist + w:
#                         dist[nei] = cur_dist + w
#                         heapq.heappush(heap, (dist[nei], nei))
            
#             return sum(1 for d in dist if 0 < d <= distanceThreshold)

#         res, min_count = -1, n
#         for src in range(n):
#             count = dijkstra(src)
            
#             if count <= min_count:
#                 res = src
#                 min_count = count

#         return res


# Using Floyd-Warshall Algorithm


class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        
        dist = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        min_count = n
        result = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            if count <= min_count:
                min_count = count
                result = i

        return result




solution = Solution()
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
threshold = 4
print(solution.findTheCity(n, edges, threshold)) 