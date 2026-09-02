class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string, int> m;

        int maxSum = INT_MAX;
        vector<string> ans;

        for (int i = 0; i < list1.size(); i++) {
            m[list1[i]] = i;
        }
        for (int i = 0; i < list2.size(); i++) {
            if (m.count(list2[i])) {
                int sum = m[list2[i]] + i;

                if (sum < maxSum) {
                    maxSum = sum;
                    ans.clear();
                    ans.push_back(list2[i]);
                } else if (sum == maxSum) {
                    ans.push_back(list2[i]);
                }
            }
        }

        return ans;
    }
};
