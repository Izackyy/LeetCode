class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        int n = nums.size() - 1;
        int prodLeft = nums[0] * nums[1] * nums[2];
        int prodRight = nums[0] * nums[n] * nums[n - 1];

        return max(prodLeft, prodRight);
    }
};
