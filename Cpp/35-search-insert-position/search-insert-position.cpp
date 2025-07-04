class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return binarySearch(nums, target, 0, nums.size() - 1);
    }
private:
    int binarySearch(vector<int>& nums, int target, int lower, int upper) {
        
        if (lower > upper) 
            return lower;
        
        int mid = lower + (upper - lower) / 2;

        if (nums[mid] == target) {
            return mid;
        } 
        else if (nums[mid] > target) {
            return binarySearch(nums, target, lower, mid - 1);
        }
        else {
            return binarySearch(nums, target, mid + 1, upper);
        }
    }
};