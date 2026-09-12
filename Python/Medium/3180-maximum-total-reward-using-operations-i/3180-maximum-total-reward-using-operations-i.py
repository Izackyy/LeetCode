class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        rewardValues.sort()
        n = len(rewardValues)
        max_possible_score = 2 * rewardValues[n - 1]

        preDP = [False] * (max_possible_score + 1)
        currDP = [False] * (max_possible_score + 1)
        preDP[0] = True

        for i in range(n):
            for j in range((rewardValues[i])):
                if preDP[j]:
                    currDP[j + (rewardValues[i])] = True

            for k in range(len(preDP)):
                if currDP[k]:
                    preDP[k] = True
                currDP[k] = False

        for i in range(len(preDP) - 1, -1, -1):
            if preDP[i]:
                return i

        return 0
