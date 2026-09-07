class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_list = collections.defaultdict(list)
        prereq_count = collections.defaultdict(int)

        for u, v in prerequisites:
            adj_list[u].append(v)
            prereq_count[v] += 1

        queue = deque([node for node in range(numCourses) if prereq_count[node] == 0])
        ans = []

        while queue:
            curr = queue.popleft()
            ans.append(curr)

            for neighbour in adj_list[curr]:
                prereq_count[neighbour] -= 1

                if prereq_count[neighbour] == 0:
                    queue.append(neighbour)

            
        return ans[::-1] if len(ans) == numCourses else []