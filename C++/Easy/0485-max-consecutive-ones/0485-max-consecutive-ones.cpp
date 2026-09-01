class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0, count1 = 0;
        
        for (int i = 0; i < size(nums); i++) {
            if (nums[i] == 1) {
                count++;
            } else {
                count1 = max(count, count1);
                count = 0;
            }
        }
        
        return max(count, count1);
    }
};
