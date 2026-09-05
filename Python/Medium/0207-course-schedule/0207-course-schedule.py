from collections import deque, defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = defaultdict(list)
        prereq_count = defaultdict(int)

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            prereq_count[course] += 1


        queue = deque([c for c in range(numCourses) if prereq_count[c] == 0])
        courses_taken = 0

        while queue:
            curr = queue.popleft()
            courses_taken += 1

            for c in adj_list[curr]:
                prereq_count[c] -= 1

                if prereq_count[c] == 0:
                    queue.append(c)
        
        return courses_taken == numCourses
            