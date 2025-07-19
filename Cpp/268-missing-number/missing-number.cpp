class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int xor_all = 0;
        int xor_nums = 0;

        for (int i = 1; i <= nums.size(); i++) {
            xor_all ^= i;
            xor_nums ^= nums[i - 1];
        }

        return xor_all ^ xor_nums;
    }
};