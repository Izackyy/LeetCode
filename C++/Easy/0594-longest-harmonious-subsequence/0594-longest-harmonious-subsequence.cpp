class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> m;

        int count = 0, maxCount = 0;

        for (int n : nums) {
            m[n] += 1;
        }

        for (int n : nums) {
            if (m[n + 1] > 0) {
                count = m[n] + m[n + 1];
            }
            maxCount = max(maxCount, count);
        }

        return maxCount;
    }
};
