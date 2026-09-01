class Solution {
public:
    int thirdMax(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());

        int dist_count = 1;
        int prev_num = nums[0];

        for (int i = 1; i < nums.size(); i++) { 
            
            if (prev_num != nums[i]) {
                dist_count++;
                prev_num = nums[i];
            }
            
            if (dist_count == 3) {
                return nums[i];
            }
        }

        return nums[0];
    }
};
