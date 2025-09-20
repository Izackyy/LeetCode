class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && (nums[i] == nums[i - 1])) {
                continue;
            }
            for (int j = i + 1; j < nums.size(); j++) {
                if (j > i + 1 && (nums[j] == nums[j - 1])) {
                    continue;
                }

                int sum_ij = nums[i] + nums[j];
                int left =  j + 1, right = nums.size() - 1;

                while (left < right) {
                    long long sum = (long long) sum_ij + nums[left] + nums[right];

                    if (sum < target) {
                        left++;
                    } else if (sum > target) {
                        right--;
                    } else {
                        result.push_back({nums[i], nums[j], nums[left], nums[right]});
                        left++;

                        while ((left < right) && (nums[left] == nums[left - 1])) {
                            left++;
                        }
                    }
                }
            }
        }

        return result;
    }
};