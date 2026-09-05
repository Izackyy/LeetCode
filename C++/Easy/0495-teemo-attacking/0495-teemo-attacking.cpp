class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int count = 0;
        if (size(timeSeries) == 0) {
            return 0;
        }

        for (int i = 0; i < size(timeSeries) - 1; i++) {
            count += min(timeSeries[i + 1] - timeSeries[i], duration);
        }

        return count + duration;
    }
};
