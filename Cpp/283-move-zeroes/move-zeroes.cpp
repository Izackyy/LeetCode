class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        if (nums.size() == 1 && nums[0] == 0)
            return;
        
        int i = 0, j = 0;
        while (j < nums.size()) {
            if (nums[j] != 0) {
                nums[i] = nums[j];
                if (i != j) {
                    nums[j] = 0;
                }
                i++;
            }
            j++;
        }
    }
};
