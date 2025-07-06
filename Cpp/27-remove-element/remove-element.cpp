class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int cur = nums.size() - 1;
        int i = 0;
        int temp;

        if (nums.empty())
            return 0;

        while (i < cur + 1) {
            if (nums[i] == val) {
                temp = nums[cur];
                nums[cur] = nums[i];
                nums[i] = temp;
                cur--;
            }
            else {
                i++;
            }
        }

        return i;
    }
};