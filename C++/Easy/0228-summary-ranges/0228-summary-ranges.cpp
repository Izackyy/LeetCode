class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> s;
        if (nums.empty())
            return s;

        int start = nums[0];


        for (int i = 1; i <= nums.size(); i++) {
            if (i == nums.size() || static_cast<long long>(nums[i]) - nums[i - 1] > 1) {
                if (nums[i - 1] == start) {
                    s.push_back(to_string(start));
                }
                else {
                    s.push_back(to_string(start) + "->" + to_string(nums[i - 1]));
                }

                if (i < nums.size())
                    start = nums[i];
            }
        }
        return s;
    }
};
