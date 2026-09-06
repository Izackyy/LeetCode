class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj_list = collections.defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))

        max_time = 0
        pq = [(0, k)]
        visited = set()

        while pq:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue
            
            visited.add(node)
            max_time = max(max_time, time)

            for neighbour, weight in adj_list[node]:
                if neighbour not in visited:
                    heapq.heappush(pq, (time + weight, neighbour))

        return max_time if len(visited) == n else -1