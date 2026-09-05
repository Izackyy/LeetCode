class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        
        canOpen = True
        ans = 0

        while initialBoxes and canOpen:
            canOpen = False
            nextBoxes = []

            for box in initialBoxes:
                if status[box]:
                    canOpen = True
                    nextBoxes.extend(containedBoxes[box])
                    for key in keys[box]:
                        status[key] = 1
                    ans += candies[box]                    
                else:
                    nextBoxes.append(box)
            initialBoxes = nextBoxes

        return ans
        