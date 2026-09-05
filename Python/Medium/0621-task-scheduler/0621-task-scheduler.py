from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = 0
        for val in freq.values():
            if val == max_freq:
                max_count += 1
        
        min_time = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), min_time)