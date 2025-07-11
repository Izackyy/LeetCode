class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); i++) {
            if (map.count(nums[i])) {
                return true;
            }
            else {
                map[nums[i]] = nums[i];
            }
        }

        return false;
    }
};