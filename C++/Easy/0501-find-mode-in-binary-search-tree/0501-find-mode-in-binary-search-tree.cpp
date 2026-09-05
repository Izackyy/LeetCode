/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> values;
        dfs(root, values);

        int curr_streak = 0, max_streak = 0;
        int curr_num = 0;
        vector<int> ans;

        for (int num : values) {
            if (num == curr_num) {
                curr_streak++;
            } else {
                curr_streak = 1;
                curr_num = num;  
            }
            if (curr_streak > max_streak) {
                ans = {};
                max_streak = curr_streak;
            }
            if (curr_streak == max_streak) {
                ans.push_back(num);
            }
        }

        return ans;
    }

    void dfs (TreeNode* node, vector<int>& values) {
        if (node == nullptr) {
            return;
        }

        dfs(node->left, values);
        values.push_back(node->val);
        dfs(node->right, values);
    }
};
