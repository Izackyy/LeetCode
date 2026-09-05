class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int actualSum = n * (n + 1) / 2;
        int uniqueSum = 0;
        int arraySum = 0;
        unordered_set<int> s(nums.begin(), nums.end());

        for (int n : nums) {
            arraySum += n;
        }

        for (int n : s) {
            uniqueSum += n;
        }

        int duplicate = arraySum - uniqueSum;
        int missing = actualSum - uniqueSum;

        return {duplicate, missing};
    }

};
