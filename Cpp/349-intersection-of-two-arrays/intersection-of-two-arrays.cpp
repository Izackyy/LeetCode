class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set;
        unordered_set<int> resultSet;

        for (int num : nums1) {
            set.insert(num);
        }
        for (int num : nums2) {
            if (set.count(num)) {
                resultSet.insert(num);
            }
        }
        vector<int> result(resultSet.begin(), resultSet.end());
        return result;
    }
};