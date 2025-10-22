from collections import defaultdict, deque

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        dist = [float('inf')] * n
        dist[src] = 0

        queue = deque()
        queue.append((src, 0))

        stops = 0
        while queue and stops <= k:
            size = len(queue)
            temp_dist = dist[:]
            for _ in range(size):
                node, cost = queue.popleft()
                for neighbor, price in adj[node]:
                    if cost + price < temp_dist[neighbor]:
                        temp_dist[neighbor] = cost + price
                        queue.append((neighbor, cost + price))
            dist = temp_dist
            stops += 1

        return dist[dst] if dist[dst] != float('inf') else -1



solution = Solution()
print(solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,3,100],[0,2,500]], 0, 3, 1))